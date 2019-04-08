from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree, number_of_nodes
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from model.optimize import maximum_entropy

# Red distribution (uniform or single)
uniform = False
airports, routes = load_airport_and_route(deep_load=True)     # Import data

# Import data and generate network
netx = from_edgelist(routes)
N = number_of_nodes(netx)
net = network(N, graph=netx)
budget = balls_per_node * N
print('Data imported and network generated')

# Initialize opponent distribution
if uniform:
    red = array([balls_per_node] * N)
else:
    degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]
    max_d_node = argmax(degrees)
    red = zeros(N)
    red[max_d_node] = budget

# Set initial distribution
net.set_initial_distribution(red=red)

# Run metric
maximum_entropy(net, metric_id=1)
exposures = run_polya(net)

# Calculate number of nodes that were allocated balls
B = [node.black for node in net.nodes]
non_zero = 0
for Bi in B:
    if Bi > 0: non_zero += 1
print('Number of allocated nodes ' + str(non_zero))

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
data_name = '../../data/max_entropy/opt_' + file_name + '.csv'

# Save and plot data
save_trials(exposures, data_name, single_line=True)
