from random import randint
from utilities import balls_added
from copy import deepcopy


# Run one time-step of Polya
# TODO Ensure that polya is running as expected
# TODO Add multi-threading
# TODO look at way of removing the need to perform a deep copy
def run_polya(network, steps):
    delta_balls = steps * balls_added
    next_network = deepcopy(network)                        # Make copy of network
    for i, node in enumerate(network):                      # For each (original) node
        drawn_ball = choose_ball(node, delta_balls)         # draw ball
        next_network[i].add_ball(drawn_ball)   # Add new ball to next network

    return next_network


# Choose ball for given node
def choose_ball(target_node, delta_balls):
    num_balls = target_node.total_balls + delta_balls   # Total number of balls in current node
    total_balls = target_node.super_urn_balls + delta_balls * target_node.degree

    ball_choice = randint(0, total_balls-1)   # Go from ball number to index (1...n vs 0...(n-1))

    if ball_choice < num_balls:                     # If ball is in target node
        return target_node.get_ball(ball_choice)    # Return ball colour

    # If ball chosen in not in current node
    ball_index = ball_choice - num_balls

    for neighbour in target_node:  # For each neighbour of node
        neighbour_total = neighbour.total_balls + delta_balls       # Node starting balls + number added through sym

        if ball_index < neighbour_total:    # If the index is less then the number of balls in node
            return neighbour.get_ball(ball_index)

        ball_index -= neighbour_total

    print('Blow')
    return 'b'
