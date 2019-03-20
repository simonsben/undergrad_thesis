from utilities.plotting import plot_net_w_routes
from execute.import_data import load_airport_and_route
from utilities import filter_degree, re_index
from networkx import degree, from_edgelist
from numpy import argmax
from utilities import dict_to_arr

# Load data
airports, routes = load_airport_and_route(deep_load=True, filter_data=False)
print('Data filtered')

# Define paths
base_path = '../../results/network/'
raw_path = base_path + 'network.png'
filtered_path = base_path + 'filtered_network.png'
all_red_path = base_path + 'all_red.png'
one_red_path = base_path + 'one_red.png'

# Plot original data
plot_net_w_routes(airports, routes, plot_edges=False, file_name=raw_path, blocking=False)

# Filter data
airports, _, routes = filter_degree(airports, routes)
re_index(airports, routes)

# Plot filtered data
plot_net_w_routes(airports, routes, plot_edges=False, file_name=filtered_path, blocking=False)

# Plot all red
plot_net_w_routes(airports, routes, plot_edges=False, file_name=all_red_path, blocking=False, single=None)

# Plot one red
degrees = dict_to_arr(degree(from_edgelist(routes)))    # Get list of degrees
max_index = argmax(degrees)                             # Get max node index
plot_net_w_routes(airports, routes, plot_edges=False, file_name=one_red_path, single=max_index)
