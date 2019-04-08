from execute.import_data import load_airport_and_route
from utilities import filter_degree, re_index, dict_to_arr
from utilities.plotting import plot_network
from networkx import from_edgelist, degree

# Define cut-off for number of nodes
cut_off = 100

# Import data and filter
nodes, edges = load_airport_and_route(deep_load=True, filter_data=False)
nodes, _, edges = filter_degree(nodes, edges, d_cut_off=cut_off)
nodes, edges = re_index(nodes, edges)
print('Data imported and filtered')

# Calculate node degrees
netx = from_edgelist(edges)
degrees = dict_to_arr(degree(netx))

# Plot network
plot_network(netx, netx_plot=True, weights=degrees, plot_edges=True)
