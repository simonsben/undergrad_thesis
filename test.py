from network import network
from networkx import closeness_centrality
from utilities import dict_to_list
# from plot import animate_network
from plot import plot_contagion, plot_network

net = network(1000)
# animate_network(net)
# net.run_n_steps(250)
#
# plot_contagion(net)
closeness = closeness_centrality(net.network_plot)
close_list = dict_to_list(closeness)
plot_network(net.network_plot, close_list)

