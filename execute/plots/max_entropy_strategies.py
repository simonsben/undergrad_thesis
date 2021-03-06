from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from utilities.plotting import plot_infection
from execute.import_data import load_airport_and_route
from model.optimize import metric_names, maximum_entropy
from execute.optimal_distribution import optimal_distribution

# Red distribution (uniform or single)
uniform = False
airports, routes = load_airport_and_route(deep_load=True)     # Import data
N = len(airports)                               # Initialize N
budget = balls_per_node * N

netx = from_edgelist(routes)                    # Generate networkx network
net = network(N, graph=netx)                    # Generate network
print('Data imported and network generated')

degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]
max_d_node = argmax(degrees)                    # Get index of max degree
optimal = optimal_distribution(deep_load=True)  # Get optimal distribution


if uniform:
    red = array([balls_per_node] * N)
else:
    red = zeros(N)
    red[max_d_node] = budget
net.set_initial_distribution(red=red)

exposures = []

# Run basic metrics
for metric_id, _ in enumerate(metric_names):
    maximum_entropy(net, metric_id=metric_id)
    exposures.append(run_polya(net))

# Run optimal strategy
net.set_initial_distribution(black=optimal)
exposures.append(run_polya(net))

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/max_entropy/' + file_name + '.png'
data_name = '../../data/max_entropy/' + file_name + '.csv'
labels = metric_names + ['Optimal']

# Save and plot data
save_trials(exposures, data_name, titles=labels)
plot_infection(exposures, leg=labels, multiple=True, file_name=img_name)
