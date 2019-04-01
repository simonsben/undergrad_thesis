from networkx import barabasi_albert_graph
from time import time
from utilities.plotting import plot_scatter_data
from utilities import save_trials, balls_per_node
from model import optimize_distribution
from numpy import array, logspace
from model import network

img_name = '../../results/algorithm_performance/bonmin.png'
data_path = '../../data/algorithm_performance/bonmin.csv'

net_sizes = logspace(1, 3, 10)
optimize_times = []
trials = 10

for raw_size in net_sizes:
    size = int(raw_size)
    netx = barabasi_albert_graph(size, 5)
    net = network(size, graph=netx)
    neighbourhoods = [[neigh.id for neigh in node] for node in net.nodes]
    init_dist = [balls_per_node] * size
    budget = balls_per_node * size

    tmp = 0
    for i in range(trials):

        start = time()
        optimize_distribution(neighbourhoods, init_dist, init_dist, budget)
        end = time()
        tmp += end - start

    optimize_times.append(tmp / trials)
    print('Done ' + str(size))


data = array([net_sizes, optimize_times])
save_trials(optimize_times, data_path, titles=net_sizes, single_line=True)
plot_scatter_data(data, file_name=img_name, x_label='Network Size', y_label='Time to Optimize (s)')

