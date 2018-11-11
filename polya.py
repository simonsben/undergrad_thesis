from random import randint
from utilities import balls_added
from itertools import repeat


# Run one time-step of Polya
# TODO Add multi-threading
# TODO look at way of removing the need to perform a deep copy
def run_polya(network, steps, pool):
    num_red, num_black = 0, 0
    delta_balls = steps * balls_added

    balls = pool.starmap(choose_ball, zip(network, repeat(delta_balls), repeat(steps)))
    for i, ball in enumerate(balls):
        network[i].add_ball(ball)
        if ball == 'r':
            num_red += 1
        else:
            num_black += 1

    # for i, node in enumerate(network):                      # For each (original) node
    #
    #     drawn_ball = choose_ball(node, delta_balls, steps)         # draw ball
    #
    #     network[i].add_ball(drawn_ball)   # Add new ball to next network

    print('Steps', steps, 'red', num_red, 'black', num_black)


# Choose ball for given node
def choose_ball(target_node, delta_balls, steps):
    num_balls = target_node.total_balls + delta_balls   # Total number of balls in current node
    total_balls = target_node.super_urn_balls + delta_balls * target_node.degree    # Num balls in super urn

    ball_choice = randint(0, total_balls-1)         # Go from ball number to index (1...n vs 0...(n-1))

    if ball_choice < num_balls:                     # If ball is in target node
        return target_node.get_ball(ball_choice, steps)    # Return ball colour

    # If ball chosen in not in current node
    ball_index = ball_choice - num_balls

    for neighbour in target_node:                                   # For each neighbour of node
        neighbour_total = neighbour.total_balls + delta_balls       # Node starting balls + number added through sym

        if ball_index < neighbour_total:    # If the index is less then the number of balls in node
            return neighbour.get_ball(ball_index, steps)

        ball_index -= neighbour_total

    raise IndexError('Ball index chosen greater than bounds of nodes')
