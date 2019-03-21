from networkx import barabasi_albert_graph
from time import time
from utilities.plotting import plot_scatter_data
from utilities import save_trials
from model.optimize import simple_centrality, maximum_entropy, gradient_optimize
from numpy import array
from model import network

img_name = '../../results/algorithm_performance/gradient.png'
data_path = '../../data/algorithm_performance/gradient.csv'

net_sizes = [10, 20, 30, 50, 100, 150, 200, 250, 500, 750, 1000]
optimize_times = []
trials = 10

for size in net_sizes:
    netx = barabasi_albert_graph(size, 1)

    tmp = 0
    for i in range(trials):
        net = network(size, graph=netx)

        # start = time()
        # simple_centrality(net, 2, quiet=True)
        # # maximum_entropy(net, metric_id=1, quiet=True)
        # end = time()

        start = time()
        gradient_optimize(net)
        end = time()
        tmp += end - start

    optimize_times.append(tmp / trials)
    print('Done ' + str(size))


data = array([net_sizes, optimize_times])
save_trials(optimize_times, data_path, titles=net_sizes, single_line=True)
plot_scatter_data(data, file_name=img_name, x_label='Network Size', y_label='Time to Optimize (ns)')

