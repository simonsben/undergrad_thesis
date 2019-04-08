from model import network
from utilities import balls_per_node, save_trials, dict_to_arr
from networkx import from_edgelist, degree, number_of_nodes
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from model.optimize import simple_cliques
from numpy import argmax, array, zeros

# Red distribution (uniform or single)
uniform = False
steps = 250

# Import data and generate network
_, routes = load_airport_and_route(deep_load=True)     # Import data
netx = from_edgelist(routes)                    # Generate networkx network
N = number_of_nodes(netx)
net = network(N, graph=netx)                    # Generate network
budget = balls_per_node * N
print('Data imported and network generated')

# Initialize opponent distribution
if uniform:
    red = array([balls_per_node] * N)
else:
    degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]
    max_d_node = argmax(degrees)                    # Get index of max degree
    red = zeros(N)
    red[max_d_node] = budget


# Run basic metrics
simple_cliques(net, 92, budget)
net.set_initial_distribution(red=red)
exposures = run_polya(net, steps=steps)

# Save and plot data
file_name = 'uniform_red' if uniform else 'single_red'
data_name = '../../data/clique/' + file_name + '.csv'
save_trials(exposures, data_name, single_line=True)
