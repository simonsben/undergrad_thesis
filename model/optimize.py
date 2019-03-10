from utilities import get_node, increment_values, balls_per_node, dict_to_tuples
from math import ceil
from random import randint
from networkx import eigenvector_centrality
from numpy import zeros


def get_optimization_method(method):
    if method in methods:
        print('Running', method_names.get(method))
        return methods.get(method)

    print('Not found, running', method_names.get(0))
    return gradient_optimize


def gradient_optimize(network):
    current_exposure = network.trial_exposure[network.steps]

    while True:
        min_node, _, urn_counts = get_node(network, False)

        if network.nodes[min_node].red - 1 < 0:
            break
        network.nodes[min_node].red -= 1
        network.nodes[min_node].init_total -= 1
        increment_values(min_node, network, urn_counts, -1)

        max_node, exposure_change, _ = get_node(network, True)

        if exposure_change <= 0 or min_node == max_node:
            network.nodes[min_node].red += 1
            network.nodes[min_node].init_total += 1
            break

        increment_values(max_node, network, urn_counts, 1)
        network.nodes[max_node].red += 1
        network.nodes[max_node].init_total += 1
        current_exposure += exposure_change

        # print(current_exposure)
    print(urn_counts)


# total = m(d1 + d2 + ... + dn)
def heuristic_optimize(network):
    total = 0
    num_balls = network.n * balls_per_node
    for node in network.nodes:
        total += node.degree if node.degree > 1 else 0

    m = num_balls / total
    node_list = sorted(network.nodes, key=lambda n: n.degree, reverse=True)

    for node in node_list:
        node_balls = ceil(m * node.degree) if num_balls > 0 else 0
        num_balls -= node_balls
        if num_balls < 0:
            node_balls += num_balls
            num_balls = 0

        node.red = node_balls


def random_optimize(network):
    budget = network.n * balls_per_node
    for i, _ in enumerate(network.nodes):
        node_balls = randint(0, 20) if budget > 0 else 0
        budget -= node_balls
        if budget < 0:
            budget = 0
            node_balls += budget

        network.nodes[i].red = node_balls

    if budget > 0:
        network.nodes[len(network.nodes)-1].red = budget


def centrality_allocation(network, netx_graph=False):
    netx = network.network_plot if not netx_graph else network
    N = len(network)
    budget = balls_per_node * N

    # Calculate and sort centrality
    centralities = dict_to_tuples(eigenvector_centrality(netx))
    centralities = sorted(centralities, key=lambda c: c[1], reverse=True)

    # Generate list of node neighbours
    neighbourhoods = [[neigh.id for neigh in node] for node in network.nodes]
    ball_counts = zeros((N, 2))
    ball_allocations = []

    # Super-urn ball counts
    for i, node in enumerate(network.nodes):
        ball_counts[i] = (node.red, 0)

        for neigh in neighbourhoods[i]:
            ball_counts[i, 0] += network.nodes[neigh].red

    # Place black in super urns
    for (ind, _) in centralities:
        tmp = ball_counts[ind, 0]
        num_added = tmp if budget > tmp else budget
        budget -= num_added

        ball_allocations.append((ind, num_added))

        ball_counts[ind, 1] += num_added
        for neigh in neighbourhoods[ind]:
            ball_counts[neigh, 1] += num_added

        if budget == 0:
            break

    # Distribute remainder of balls
    if budget > 0:
        max_ind = centralities[0][0]
        ball_counts[max_ind, 1] += budget
        ball_allocations[0][1] += budget

        for neigh in neighbourhoods[max_ind]:
            ball_counts[neigh, 1] += budget

    black_dist = zeros(N)
    for (ind, alloc) in ball_allocations:
        black_dist[ind] = alloc

    network.set_initial_distribution(black=black_dist)


method_names = {
    0: 'Gradient Descent',
    1: 'Heuristic',
    2: 'Random',
    3: 'Centrality allocation'
}

methods = {
    0: gradient_optimize,
    1: heuristic_optimize,
    2: random_optimize,
    3: centrality_allocation
}
