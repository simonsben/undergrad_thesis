from model import network
from utilities import balls_per_node, save_trials
from networkx import from_edgelist, degree, number_of_nodes
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from execute.optimal_distribution import optimal_distribution

# Choose simulation options
uniform = False
num_steps = 250

# Load data and generate network
_, routes = load_airport_and_route(deep_load=True)
netx = from_edgelist(routes)
N = number_of_nodes(netx)
net = network(N, graph=netx)
budget = balls_per_node * N
print('Data imported and network generated')

# Get optimal distribution
optimal = optimal_distribution(uniform, deep_load=True)

# Initialize opponent distribution
if uniform:
    red = array([balls_per_node] * N)
else:
    degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]
    max_d_node = argmax(degrees)
    red = zeros(N)
    red[max_d_node] = budget


# Run optimal strategy
net.set_initial_distribution(black=optimal, red=red)
exposures = run_polya(net, steps=num_steps)

# Define constants
file_name = ('uniform_red' if uniform else 'single_red') + '_trial'
data_name = '../../data/optimal_distribution/' + file_name + '.csv'

# Save and plot data
save_trials(exposures, data_name, single_line=True)
