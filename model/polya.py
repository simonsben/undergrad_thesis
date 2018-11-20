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


