from execute.import_data import load_airport_and_route
from execute.optimal_distribution import optimal_distribution
from utilities.plotting import plot_net_w_routes, plot_network
from networkx import from_edgelist


airports, routes = load_airport_and_route(deep_load=True)
weights = optimal_distribution(deep_load=True)

path = '../../results/network/optimal.png'
# plot_net_w_routes(airports, routes, plot_edges=False, weights=weights, file_name=path)
netx = from_edgelist(routes)
plot_network(netx, netx_plot=True, weights=weights, file_name=path)
