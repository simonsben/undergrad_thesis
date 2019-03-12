from model.network import network
from numpy import array
from utilities import plot_w_best_fit
from time import time_ns


def sum_by_degree(_network):
    ball_dist = {}
    for i, node in enumerate(_network.nodes):
        degree = node.degree
        if degree in ball_dist:
            ball_dist[degree] = (node.red + ball_dist[degree][0], ball_dist[degree][1] + 1)
        else:
            ball_dist[degree] = (node.red, 1)

    return ball_dist


def merge_dict(dict_a, dict_b):
    for item in dict_b:
        if item in dict_a:
            dict_a[item] += dict_b[item]
        else:
            dict_a[item] = dict_b[item]

    return dict_a


num_trials = 150
network_size = 150

start = time_ns()
count = {}
for i in range(num_trials):
    net = network(network_size)
    net.optimize_initial()

    trial_count = sum_by_degree(net)
    count = merge_dict(count, trial_count)

    print('Trial', i+1, 'done', (i+1)/num_trials*100, '%  complete')

end = time_ns()
print('Time to compute = ', (end - start) / 1000000000 / 60)

count_list = array([(degree, count[degree][0] / count[degree][1]) for degree in count])

plot_w_best_fit(count_list, 'Average number of balls vs degree of node', '../results/balls_vs_degree_' +
                str(network_size) + '.png', False, 'Node degree', 'Average number of red balls',
                data_name='../data/balls_vs_degree_' + str(network_size) + '.csv')
