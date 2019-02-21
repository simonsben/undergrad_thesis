from model.extension import extend_network
from networkx import barabasi_albert_graph
from utilities.plot import plot_network

NUM_NODES = 20
EDGE_COUNT = 1

network = barabasi_albert_graph(NUM_NODES, EDGE_COUNT)
plot_network(network, save_plot=False, netx_plot=True, blocking=False, _title='Raw Graph')

extend_network(network)
plot_network(network, save_plot=False, netx_plot=True, _title='Extended graph')
