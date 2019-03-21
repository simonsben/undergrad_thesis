from execute.import_data import load_airport_and_route
from networkx import from_edgelist, betweenness_centrality, number_of_nodes
from utilities import dict_to_arr, re_index, balls_per_node
from numpy import array
from utilities.plotting import plot_network

# Define constants
cut_off = 25
fig_path = '../../results/centrality_metrics/slim.png'

# Import data and generate network
nodes, edges = load_airport_and_route(deep_load=True)
netx = from_edgelist(edges)

# Calculate betweenness
cents = dict_to_arr(betweenness_centrality(netx), conv=False)
cents = array(sorted(cents, key=lambda c: c[1], reverse=True))

# Pull nodes
slim_set = []
for i in range(cut_off):
    ind = int(round(cents[i, 0]))
    print(ind)
    slim_set.append(nodes[ind])
slim_set = array(slim_set)

# Filter old edges
n_nodes, n_edges = re_index(slim_set, edges)
n_netx = from_edgelist(n_edges)

# Generate ball distribution
N = number_of_nodes(netx)
budget = balls_per_node * N
total = sum(cents[:cut_off, 1])
B = [0] * cut_off
for i in range(cut_off):
    B[i] = cents[i, 1] / total * budget

# Plot network
plot_network(n_netx, netx_plot=True, plot_edges=True, alph=.15, weights=B, file_name=fig_path, size=(10, 5))
