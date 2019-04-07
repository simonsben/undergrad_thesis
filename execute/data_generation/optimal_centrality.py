from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from model.optimize import simple_centrality

# Red distribution (uniform or single)
uniform = False
steps = 250
airports, routes = load_airport_and_route(deep_load=True)     # Import data
N = len(airports)                               # Initialize N
budget = balls_per_node * N

netx = from_edgelist(routes)                    # Generate networkx network
net = network(N, graph=netx)                    # Generate network
print('Data imported and network generated')

degrees = array(sorted(degree(netx), key=lambda d: d[1]))[:, 1]
max_d_node = argmax(degrees)                    # Get index of max degree

if uniform:
    red = array([balls_per_node] * N)
else:
    red = zeros(N)
    red[max_d_node] = budget


# Run basic metrics
simple_centrality(net, 2, red=red, node_restriction=11)
exposures = run_polya(net, steps=steps)

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
data_name = '../../data/centrality_metrics/opt_' + file_name + '_long.csv'

# Save and plot data
save_trials(exposures, data_name, single_line=True)
