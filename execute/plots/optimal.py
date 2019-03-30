from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from execute.optimal_distribution import optimal_distribution

# Red distribution (uniform or single)
uniform = True
num_steps = 250
airports, routes = load_airport_and_route(deep_load=True)     # Import data
N = len(airports)                               # Initialize N
budget = balls_per_node * N

netx = from_edgelist(routes)                    # Generate networkx network
net = network(N, graph=netx)                    # Generate network
print('Data imported and network generated')

degrees = dict_to_arr(degree(netx))             # Calculate node degrees
max_d_node = argmax(degrees)                    # Get index of max degree
optimal = optimal_distribution(deep_load=True)

if uniform:
    red = array([balls_per_node] * N)
else:
    red = zeros(N)
    red[max_d_node] = budget

exposures = []

# Run optimal strategy
net.set_initial_distribution(black=optimal, red=red)
exposures.append(run_polya(net, steps=num_steps))

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/optimal_distribution/' + file_name + '.png'
data_name = '../../data/optimal_distribution/' + file_name + '.csv'
labels = ['Optimal']

# Save and plot data
save_trials(exposures, data_name, titles=labels)
