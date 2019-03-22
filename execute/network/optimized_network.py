from execute.import_data import load_airport_and_route
from execute.optimal_distribution import optimal_distribution
from utilities.plotting import plot_net_w_routes, plot_network
from networkx import from_edgelist
from utilities import filter_degree, re_index
from numpy import max, min, multiply, add

data_path = '../../data/optimal_distribution/f_100_analytical.csv'
airports, routes = load_airport_and_route(deep_load=True, filter_data=False)
airports, _, routes = filter_degree(airports, routes, d_cut_off=100)
airports, routes = re_index(airports, routes)
weights = optimal_distribution(alt_file=data_path)

min_val, max_val = min(weights), max(weights)
delt = max_val - min_val
weights = multiply(add(weights, -min_val), 1/delt)

print(len(airports))

path = '../../results/network/optimal.png'
# plot_net_w_routes(airports, routes, plot_edges=False, weights=weights, file_name=path)
netx = from_edgelist(routes)
plot_network(netx, netx_plot=True, weights=weights, file_name=path, plot_edges=True, size=(10, 6))
