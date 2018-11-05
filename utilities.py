from numpy import zeros

# Define constants
network_memory = 10000
balls_added = 1
balls_per_node = 10


def dict_to_list(_dict):
    new_list = []
    for _, value in _dict.items():
        new_list.append(value)

    return new_list
