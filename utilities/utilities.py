# Define constants
network_memory = 10000
balls_added = 1
balls_per_node = 10
min_steps = 8000
min_trials = 30


# Method to convert a dict to a list (for plotting)
def dict_to_list(_dict):
    new_list = []
    for _, value in _dict.items():
        new_list.append(value)

    return new_list


# Method to return default budget for a given graph
def calculate_budget(n):
    return int(balls_per_node / 2) * n - n
