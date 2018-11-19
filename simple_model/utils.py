from numpy import sum, copy
from sys import maxsize


def calculate_exposure(graph):
    exposure = 0
    for i, node in enumerate(graph):
        left, center, right = 0, 0, 0
        left_r, center_r,  right_r = 0, 0, 0
        left_ind, center_ind, right_ind = i-1, i, i+1

        if left_ind >= 0:
            left = sum(graph[left_ind])
            left_r = graph[left_ind][0]
        if right_ind < len(graph):
            right = sum(graph[right_ind])
            right_r = graph[right_ind][0]

        center = sum(graph[center_ind])
        center_r = graph[center_ind][0]

        exposure += sum([left_r, center_r, right_r]) / sum([left, center, right])

    return exposure


def pull_extreme(exposures, graph, func, check_max):
    indexes = []
    if check_max:
        value = - (maxsize - 1)
    else:
        value = maxsize

    for i, num in enumerate(exposures):
        if check_max and num > value or not check_max and num < value:
            if check_max or not check_max and graph[i][0] > 0:
                value = num
                indexes = [i]
        elif num == value:
            indexes.append(i)

    if len(indexes) > 1:
        options = [graph[ind][0] for ind in indexes]
        return indexes[func(options)]
    return indexes[0]


def get_node(graph, func, check_max):
    exposures = []
    for i in range(len(graph)):
        tmp_graph = copy(graph)
        tmp_graph[i][0] += 1
        tmp_exposure = calculate_exposure(tmp_graph)
        exposures.append(tmp_exposure)

    return pull_extreme(exposures, graph, func, check_max)
