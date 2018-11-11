from numpy.random import randint
from utilities import balls_added
from itertools import repeat


# Run one time-step of Polya
# TODO Add multi-threading
# TODO look at way of removing the need to perform a deep copy
def run_polya(network, steps, pool, use_threading=True):
    num_red, num_black = 0, 0
    delta_balls = steps * balls_added

    if use_threading and len(network) > 100:
        balls = pool.starmap(choose_ball, zip(network, repeat(delta_balls), repeat(steps)))
    else:
        balls = []
        for node in network:
            balls.append(choose_ball(node, delta_balls, steps))

    for i, ball in enumerate(balls):
        network[i].add_ball(ball)
        if ball == 'r':
            num_red += 1
        else:
            num_black += 1

    print('Steps', steps, 'red', num_red, 'black', num_black)


# TODO re-write this to get ratios from neighbours then just run a prob, over-complicated
# Choose ball for given node
def choose_ball(target_node, delta_balls, steps):
    num_balls = target_node.total_balls + delta_balls   # Total number of balls in current node
    total_balls = target_node.super_urn_balls + delta_balls * target_node.degree    # Num balls in super urn

    ball_choice = randint(0, total_balls+1)         # Go from ball number to index (1...n vs 0...(n-1))

    if ball_choice < num_balls:                     # If ball is in target node
        return target_node.get_ball(ball_choice, steps)    # Return ball colour

    # If ball chosen in not in current node
    ball_index = ball_choice - num_balls

    for neighbour in target_node:                                   # For each neighbour of node
        neighbour_total = neighbour.total_balls + delta_balls       # Node starting balls + number added through sym

        if ball_index <= neighbour_total:    # If the index is less then the number of balls in node
            return neighbour.get_ball(ball_index, steps)

        ball_index -= neighbour_total

    raise IndexError('Ball index chosen greater than bounds of nodes')
