from model.network import network
from utilities import plot_network

net = network(100)
plot_network(net, _title='Free-Scale Network', netx_plot=True)
