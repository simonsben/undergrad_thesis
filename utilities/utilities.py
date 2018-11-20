from networkx import barabasi_albert_graph
from numpy import zeros, mean

# Define constants
network_memory = 10000
balls_added = 1
balls_per_node = 10
min_steps = 8000
min_trials = 30
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


def calculate_exposure(network):
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

            network.node_exposures[i] = urn_counts[i, 0] / urn_counts[i, 1]

    exposure = mean(network.node_exposures)
    network.exposures.append(exposure)

    return exposure
