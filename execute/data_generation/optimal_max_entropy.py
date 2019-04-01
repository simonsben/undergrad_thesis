from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from model.optimize import maximum_entropy

# Red distribution (uniform or single)
uniform = True
airports, routes = load_airport_and_route(deep_load=True)     # Import data
N = len(airports)                               # Initialize N
budget = balls_per_node * N

netx = from_edgelist(routes)                    # Generate networkx network
net = network(N, graph=netx)                    # Generate network
print('Data imported and network generated')

degrees = dict_to_arr(degree(netx))             # Calculate node degrees
max_d_node = argmax(degrees)                    # Get index of max degree


if uniform:
    red = array([balls_per_node] * N)
else:
    red = zeros(N)
    red[max_d_node] = budget
net.set_initial_distribution(red=red)

# Run metric
maximum_entropy(net, metric_id=1)
exposures = run_polya(net)

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
