from model import network
from utilities import balls_per_node, dict_to_arr, save_trials
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from utilities.plotting import plot_infection
from execute.import_data import load_airport_and_route
from model.optimize import simple_centrality, metric_names

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

exposures = []

# Run basic metrics
for metric_id, _ in enumerate(metric_names):
    simple_centrality(net, metric_id, red=red)
    exposures.append(run_polya(net))

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/centrality_metrics/' + file_name + '_2.png'
data_name = '../../data/' + file_name + '.csv'

# Save and plot data
save_trials(exposures, data_name, titles=metric_names)
plot_infection(exposures, leg=metric_names, multiple=True, file_name=img_name)
