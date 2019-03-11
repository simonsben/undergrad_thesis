from execute.import_data import load_airport_and_route
from networkx import from_edgelist, make_max_clique_graph
from model.optimize.colapse import simplify_net
from utilities.plotting import plot_network

airports, routes = load_airport_and_route()
print('Data loaded')

netx = from_edgelist(routes)
print('Network generated')

s_net = make_max_clique_graph(netx)
print('Net simplified')

plot_network(netx, netx_plot=True, blocking=False)
plot_network(s_net, netx_plot=True)

# simplify_net(netx, netx_inp=True)
