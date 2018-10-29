from random import randint
from utilities import balls_added
from copy import deepcopy


# Run one time-step of Polya
# TODO Ensure that polya is running as expected
# TODO Add multi-threading
# TODO look at way of removing the need to perform a deep copy
def run_polya(network):
    next_network = deepcopy(network)  # Make copy of network
    for i, node in enumerate(network):  # For each (original) node
        drawn_ball = choose_ball(node)  # draw ball
        next_network[i].add_ball(drawn_ball, balls_added)  # Add new ball to next network

    return next_network


# Choose ball for given node
def choose_ball(target_node):
    # Get total number of balls in node and neighbours
    num_balls = target_node.red + target_node.black
    node_balls = [num_balls]

    for i, node in enumerate(target_node):  # For each neighbouring node
        num_balls += node.red + node.black  # Total balls in node
        node_balls.append(num_balls)  # Record cumulative number of balls

    # Choose ball
    # TODO Ensure that this is actually choosing the right ball
    ball_choice = randint(0, num_balls - 1)
    chosen_node = None
    ball_index = 0

    # Find ball
    if ball_choice < node_balls[0]:  # If ball is in target node
        chosen_node = target_node  # Choose target node
    else:
        for i, count in enumerate(node_balls):  # For each neighbouring node
            if ball_choice < count:  # If the chosen ball lies within a given node
                chosen_node = target_node.neighbours[i - 1]  # Pointer to node
                ball_index = count - ball_choice  # Index of ball in node
                break

    chosen_ball = chosen_node.get_ball(ball_index)  # Get ball

    return chosen_ball  # Return drawn ball
