from utilities import load_csv_col, filter_related_data, region, airpt_cols, rt_cols, re_index, filter_degree, balls_per_node
from utilities.plotting import plot_degree_dist
from networkx import from_edgelist, closeness_centrality
from utilities.plotting import plot_net_w_routes
from model import network
from numpy import zeros, sum

# Load airports
airports = load_csv_col('../../data/airports.dat', cols=airpt_cols)
routes = load_csv_col('../../data/routes.dat', cols=rt_cols)
print('Data loaded')

# Filter data
# airports_red, routes_red, route_indexes = filter_related_data(airports, routes, region)
# print(len(airports_red))
airports_red, routes_red, route_indexes = filter_degree(airports, routes)
re_index(airports_red, route_indexes)
print(len(airports_red))

print('Data filtered')

# plot_net_w_routes(airports_red, routes_red, plot_edges=False)

net = from_edgelist(route_indexes)
# plot_degree_dist(net, netx_src=True)
t_cent = closeness_centrality(net)
cent = zeros(len(airports_red))
for i in cent:
    cent[i] = t_cent.get(i)
cent_total = sum(cent)
print(cent)
print(cent_total)

B = balls_per_node * len(airports_red)
net_c = network(len(airports_red), net)


