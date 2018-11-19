from numpy import full, sum, argmin, copy, argmax
from simple_model.utils import calculate_exposure, get_node, pull_extreme


graph = full((5, 2), 5)
current_exposure = calculate_exposure(graph)
print('initial exposure', current_exposure)
print('--------------')


while True:
    exposures = []
    min_gradient = get_node(graph, argmax, False)

    if graph[min_gradient][0] - 1 < 0:
        print('neg val')
        break

    graph[min_gradient][0] -= 1

    max_gradient = get_node(graph, argmin, True)
    graph[max_gradient][0] += 1

    tmp_exposure = calculate_exposure(graph)

    if current_exposure >= tmp_exposure:
        print('done op')
        break

    current_exposure = tmp_exposure

print('done', graph)
