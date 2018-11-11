from network import network
from networkx import closeness_centrality
from utilities import dict_to_list
# from plot import animate_network
from plot import plot_contagion, plot_network

if __name__ == '__main__':
    net = network(10000)
    print('generated')
    # animate_network(net)
    net.run_n_steps(250)
    plot_contagion(net)

    # closeness = closeness_centrality(net.network_plot)
    # close_list = dict_to_list(closeness)
    net.calculate_weights()
    plot_network(net.network_plot, net.weights)
