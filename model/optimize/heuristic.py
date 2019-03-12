from utilities import balls_per_node
from math import ceil


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

    print('Degree heuristic calculated')
