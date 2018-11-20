from random import random
from utilities.utilities import balls_added
from itertools import repeat


# Run one time-step of Polya
def run_polya(network, steps, pool, use_threading=True):
    delta_balls = steps * balls_added

    if use_threading and len(network) > 100:
        balls = pool.starmap(choose_ball, zip(network, repeat(delta_balls), repeat(steps)))
    else:
        balls = []
        for node in network:
            balls.append(choose_ball(node, delta_balls, steps))

    for i, ball in enumerate(balls):
        network[i].add_ball(ball)


# Choose ball for given node
def choose_ball(target_node, delta_balls, step):
    total_balls = target_node.super_urn_balls + delta_balls * (target_node.degree + 1)    # Num balls in super urn
    total_red = target_node.get_red_count(step)

    for neighbour in target_node:
        total_red += neighbour.get_red_count(step)

    red_probability = total_red / total_balls
    is_red = random() <= red_probability

    if is_red:
        return 'r'
    return 'b'
