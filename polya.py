from random import randint
from utilities import balls_added


def choose_ball(target_node):
    # Get total number of balls in node and neighbours
    num_balls = target_node.red + target_node.black
    node_balls = [num_balls]

    for i, node in enumerate(target_node):  # For each neighbouring node
        num_balls += node.red + node.black  # Total balls in node
        node_balls.append(num_balls)        # Record cumulative number of balls

    # Choose ball
    ball_choice = randint(0, num_balls-1)
    chosen_node = None
    ball_index = 0

    # Find ball
    if num_balls < node_balls[0]:   # If ball is in target node
        chosen_node = target_node   # Choose target node
    else:
        for i, count in enumerate(node_balls):  # For each neighbouring node
            if num_balls < count:   # If the chosen ball lies within a given node
                chosen_node = target_node.neighbours[i-1]   # Pointer to node
                ball_index = count - ball_choice    # Index of ball in node

    chosen_ball = chosen_node.get_ball(ball_index)  # Get ball
    target_node.add_ball(chosen_ball, balls_added)   # Add ball
