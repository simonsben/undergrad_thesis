from utilities.utilities import get_node, increment_values, balls_per_node
from math import ceil


def optimize_initial(network):
    current_exposure = network.exposures[len(network.exposures)-1]

    while True:
        min_node, _, urn_counts = get_node(network, False)

        if network.nodes[min_node].red - 1 < 0:
            # print('Negative value,  breaking.')
            break
        network.nodes[min_node].red -= 1
        network.nodes[min_node].init_total -= 1
        increment_values(min_node, network, urn_counts, -1)

        max_node, exposure_change, _ = get_node(network, True)

        if exposure_change <= 0 or min_node == max_node:
            # print('Worsened exposure, breaking.')
            network.nodes[min_node].red += 1
            network.nodes[min_node].init_total += 1
            break

        increment_values(max_node, network, urn_counts, 1)
        network.nodes[max_node].red += 1
        network.nodes[max_node].init_total += 1
        current_exposure += exposure_change


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
