from execute.import_data import load_airport_and_route
from networkx import from_edgelist, betweenness_centrality, number_of_nodes
from utilities import dict_to_arr, re_index, balls_per_node
from numpy import array
from utilities.plotting import plot_network
from model import

_, edges = load_airport_and_route(deep_load=True)
netx = from_edgelist(edges)
net = netw