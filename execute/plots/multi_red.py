from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes, degree
from model import network
from execute.run_polya import run_polya
from model.optimize import simple_centrality
from utilities import balls_per_node, save_trials, fig_size
from utilities.plotting import plot_scatter_data
from numpy import array


# Define constants
red_node_limit = 20
fresh_data = False
fig_path = '../../results/analysis/multi_red.png'
data_path = '../../data/analysis/multi_red.csv'

# Import data and generate network
_, edges = load_airport_and_route(deep_load=True)
netx = from_edgelist(edges)
N = number_of_nodes(netx)
net = network(N, graph=netx)

budget = N * balls_per_node

simple_centrality(net, 2, node_restriction=11)
degrees = sorted(degree(netx), key=lambda d: d[1], reverse=True)

infections = []
for i in range(1, red_node_limit):
    R = [0] * N
    total = 0
    for j in range(i): total += degrees[j][1]
    for j in range(i): R[degrees[j][0]] += round(degrees[j][1] / total * budget)

    net.set_initial_distribution(red=R)
    infection = run_polya(net, steps=250)
    infections.append(infection[len(infection)-1])

headers = list(range(1, red_node_limit))
data = array([headers, infections])
save_trials(infections, data_path, titles=headers, single_line=True)
plot_scatter_data(data, x_label='Number of sites with red balls', y_label='Time n infection', file_name=fig_path,
                  size=fig_size, connect=True)
