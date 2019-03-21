from networkx import barabasi_albert_graph
from time import time
from utilities.plotting import plot_scatter_data
from utilities import save_trials
from model.optimize import simple_centrality, maximum_entropy, gradient_optimize
from numpy import array, logspace
from model import network

img_name = '../../results/algorithm_performance/centrality.png'
data_path = '../../data/algorithm_performance/centrality.csv'

# net_sizes = [10, 20, 30, 50, 100, 150, 200, 250, 500, 750, 1000]
net_sizes = logspace(1, 3, 10)
optimize_times = []
trials = 10

for raw_size in net_sizes:
    size = int(raw_size)
    netx = barabasi_albert_graph(size, 5)

    tmp = 0
    for i in range(trials):
        net = network(size, graph=netx)

        start = time()
        simple_centrality(net, 2, quiet=True)
        end = time()

        tmp += end - start

    optimize_times.append(tmp / trials)
    print('Done ' + str(size))


data = array([net_sizes, optimize_times])
save_trials(optimize_times, data_path, titles=net_sizes, single_line=True)
plot_scatter_data(data, file_name=img_name, x_label='Network Size', y_label='Time to Optimize (s)')
