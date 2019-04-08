from execute.import_data import load_airport_and_route
from networkx import from_edgelist, nodes, edges
from model.optimize.colapse import simplify_net
from utilities.plotting import plot_net_w_routes
from utilities import compress_graph_data
from numpy import array

# Import data
airports, routes = load_airport_and_route(deep_load=True)
print('Data loaded')

# Generate network
netx = from_edgelist(routes)
print('Network generated')

# Compress network
s_net = simplify_net(netx, netx_inp=True)
routes = array(edges(s_net))
print('Network simplified')

# Plot network
airports, routes = compress_graph_data(airports, routes, nodes(s_net))
plot_net_w_routes(airports, routes, file_name='../../results/network/simplified_network.png')
