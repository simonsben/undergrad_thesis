from utilities import balls_per_node
from numpy.random import randint


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
