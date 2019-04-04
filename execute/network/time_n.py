from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from numpy import array
from utilities.plotting import plot_network
from model import network
from execute.optimal_distribution import optimal_distribution

# Define constants
base_path = '../../results/network/'
time_1_path = base_path + 'time_1_net.png'
time_n_path = base_path + 'time_n_net.png'
fig_size = (9, 6)

# Import data
_, edges = load_airport_and_route(deep_load=True)
netx = from_edgelist(edges)
N = number_of_nodes(netx)
net = network(N, graph=netx)

# Optimize network
B = optimal_distribution(deep_load=True)
net.set_initial_distribution(black=B)

# Calculate weights and plot network
weights = array([node.red / (node.black + node.red) for node in net.nodes])
plot_network(net, blocking=False, size=fig_size, weights=weights, plot_edges=True, file_name=time_1_path)

# Run polya process
net.run_n_steps(250)

# Calculate final exposure (sanity check)
final = net.trial_exposure[len(net.trial_exposure)-1]
print('Final exposure ' + str(final))

# Calculate weights and plot final network
weights = array([node.red / (node.black + node.red) for node in net.nodes])
plot_network(net, size=fig_size, weights=weights, plot_edges=True, file_name=time_n_path)
