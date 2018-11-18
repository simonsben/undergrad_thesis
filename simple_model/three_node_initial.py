from numpy import full, sum, argmin, argmax, copy


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


graph = full((4, 2), 5)
current_exposure = calculate_exposure(graph)
print('initial exposure', current_exposure)

while True:
    exposures = []
    for i in range(len(graph)):
        tmp_graph = copy(graph)
        tmp_graph[i][0] += 1
        exposures.append(calculate_exposure(tmp_graph))

    min_ind = argmin(exposures)
    max_ind = argmax(exposures)
    if graph[min_ind][0] - 1 < 0:
        print('neg val')
        break

    graph[min_ind][0] -= 1
    graph[max_ind][0] += 1

    tmp_exposure = calculate_exposure(graph)
    print('new exposure', tmp_exposure)

    if current_exposure >= tmp_exposure:
        print('done op')
        break

print('done', graph)
