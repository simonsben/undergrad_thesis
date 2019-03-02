from utilities import get_node, increment_values, balls_per_node
from math import ceil
from random import randint


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


        print(current_exposure)
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


method_names = {
    0: 'Gradient Descent',
    1: 'Heuristic',
    2: 'Random'
}

methods = {
    0: gradient_optimize,
    1: heuristic_optimize,
    2: random_optimize
}
