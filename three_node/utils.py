from numpy import sum, copy
from sys import maxsize


# Function to calculate the exposure of the graph
def calculate_exposure(graph):
    exposure = 0                                            # Initialize exposure counter
    for i, node in enumerate(graph):                        # For each node
        left, center, right = 0, 0, 0                       # Initialize left, right, and center total sums
        left_r, center_r,  right_r = 0, 0, 0                # Initialize left, right, and center red sums
        left_ind, center_ind, right_ind = i-1, i, i+1       # Calculate left, right, and center index

        if left_ind >= 0:                   # If left exists
            left = sum(graph[left_ind])     # Calculate left sum
            left_r = graph[left_ind][0]     # Store left red value
        if right_ind < len(graph):          # If right exists
            right = sum(graph[right_ind])   # Calculate right sum
            right_r = graph[right_ind][0]   # Store red value

        center = sum(graph[center_ind])     # Calculate center sum
        center_r = graph[center_ind][0]     # Calculate center red value

        exposure += sum([left_r, center_r, right_r]) / sum([left, center, right])   # Calculate node exposure

    return exposure


# Function to get the extreme index from a set (either min or max)
def pull_extreme(exposures, graph, func, check_max):
    indexes = []                    # Initialize list of indexes
    if check_max:                   # If checking max (vs min) initialize starting value
        value = - (maxsize - 1)
    else:
        value = maxsize

    for i, num in enumerate(exposures):                                 # For each node
        if check_max and num > value or not check_max and num < value:  # If node exposure mode extreme
            if check_max or not check_max and graph[i][0] > 0:          # And non-negative (for min case)
                value = num                                             # Set new extreme value
                indexes = [i]                                           # Re-set index list
        elif num == value:                                              # If index is same as extreme, add to list
            indexes.append(i)

    if len(indexes) > 1:                                # If more then one element in extreme list
        options = [graph[ind][0] for ind in indexes]    # Calculate red ball counts
        return indexes[func(options)]                   # Take either the min or max (based on min or max func)
    return indexes[0]


# Function to get the node with min/max gradient
def get_node(graph, func, check_max):
    exposures = []                                              # Initialize list of exposures
    for i in range(len(graph)):                                 # For each node
        tmp_graph = copy(graph)                                 # Take copy of graph
        tmp_graph[i][0] += 1                                    # Add red ball to node
        tmp_exposure = calculate_exposure(tmp_graph)            # Calculate exposure
        exposures.append(tmp_exposure)                          # Add exposure to list

    return pull_extreme(exposures, graph, func, check_max)      # Return min/max exposure node index
