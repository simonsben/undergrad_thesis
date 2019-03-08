from utilities import airpt_cols, rt_cols, region, load_csv_col, filter_related_data, re_index
from networkx import from_edgelist
from model import network

airports = load_csv_col('../data/airports.dat', cols=airpt_cols)
routes = load_csv_col('../data/routes.dat', cols=rt_cols)
print('Data loaded')

# Filter data
airports_red, routes_red, route_indexes = filter_related_data(airports, routes, region)
re_index(airports_red, route_indexes)
print('Data filtered')

net = from_edgelist(route_indexes)
c_net = network(len(airports_red), net)

