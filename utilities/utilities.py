from networkx import barabasi_albert_graph
from numpy import zeros, mean, argmin, argmax
from sys import maxsize

# Define constants
network_memory = 10000
balls_added = 1
balls_per_node = 50
min_steps = 8000
min_trials = 30
extension_nodes = 8
ball_colour = {
    0: 'red',
    1: 'black'
}


# Generate new network
def generate_plot_network(n):
    return barabasi_albert_graph(n, 1)


# Method to convert a dict to a list (for plotting)
def dict_to_list(_dict):
    new_list = []
    for _, value in _dict.items():
        new_list.append(value)

    return new_list


# Method to return default budget for a given graph
def calculate_budget(n):
    return int(balls_per_node / 2) * n - n


def calculate_exposure(network, add_exposure=True, ret_counts=False):
    delta_balls = network.steps * balls_added
    ball_counts = zeros((network.n, 2))
    urn_counts = zeros((network.n, 2))

    for i in range(network.n):
        ball_counts[i, 0] = network.nodes[i].red
        ball_counts[i, 1] = network.nodes[i].init_total + delta_balls

    for i in range(network.n):
        urn_counts[i] = ball_counts[i]
        for node in network.nodes[i]:
            urn_counts[i, 0] += ball_counts[node.id, 0]
            urn_counts[i, 1] += ball_counts[node.id, 1]

            if urn_counts[i, 1] != 0:
                network.node_exposures[i] = urn_counts[i, 0] / urn_counts[i, 1]
            else:
                network.node_exposures[i] = .5

    exposure = mean(network.node_exposures)
    if add_exposure:
        network.exposures.append(exposure)

    if ret_counts:
        return urn_counts, ball_counts


# Function to get the extreme index from a set (either min or max)
def pull_extreme(exposures, urn_counts, check_max):
    indexes = []                    # Initialize list of indexes
    if check_max:                   # If checking max (vs min) initialize starting value
        value = - (maxsize - 1)
    else:
        value = maxsize

    for i, num in enumerate(exposures):                                 # For each node
        if check_max and num > value or not check_max and num < value:  # If node exposure mode extreme
            if check_max or not check_max and urn_counts[i][0] > 0:          # And non-negative (for min case)
                value = num                                             # Set new extreme value
                indexes = [i]                                           # Re-set index list
        elif num == value:                                              # If index is same as extreme, add to list
            indexes.append(i)

    if len(indexes) > 1:                                # If more then one element in extreme list
        options = [urn_counts[ind][0] for ind in indexes]    # Calculate red ball counts
        func = argmin if check_max else argmax
        return indexes[func(options)]                   # Take either the min or max (based on min or max func)
    return indexes[0]


# Function to get the node with min/max gradient
def get_node(network, check_max):
    # if len(urn_counts) == 0:
    urn_counts, ball_counts = calculate_exposure(network, False, True)
    # else:
    #     print('no')
    possible_exposures = zeros(len(network))

    for i, node in enumerate(network.nodes):
        old_exposure = urn_counts[i, 0] / urn_counts[i, 1]
        new_exposure = (urn_counts[i, 0] + 1) / (urn_counts[i, 1] + 1)
        for neighbour in node:
            new_exposure += (urn_counts[neighbour.id, 0] + 1) / (urn_counts[neighbour.id, 1] + 1)
            old_exposure += urn_counts[neighbour.id, 0] / urn_counts[neighbour.id, 1]

        possible_exposures[i] = new_exposure - old_exposure

    extreme_index = pull_extreme(possible_exposures, ball_counts, check_max)
    return extreme_index, possible_exposures[extreme_index], urn_counts


def increment_values(index, network, urn_counts, val):
    # Increment values
    urn_counts[index, 0] += val
    urn_counts[index, 1] += val
    for neighbour in network.nodes[index]:
        urn_counts[neighbour.id, 0] += val
        urn_counts[neighbour.id, 1] += val
