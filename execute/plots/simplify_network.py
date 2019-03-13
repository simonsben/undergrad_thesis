from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes, nodes
from model.optimize.colapse import simplify_net
from utilities.plotting import plot_network, plot_net_w_routes
from utilities import compress_graph_data

airports, routes = load_airport_and_route()
print('Data loaded')

netx = from_edgelist(routes)
print('Network generated')

s_net = simplify_net(netx, netx_inp=True)
print('Done simplifying')


airports, routes = compress_graph_data(airports, routes, nodes(s_net))
plot_net_w_routes(airports, routes, file_name='../../results/simplified_network.png')
