from network import network
from numpy import mean
from networkx import closeness_centrality
from utilities import dict_to_list
# from plot import animate_network
from plot import plot_contagion, plot_network

if __name__ == '__main__':
    # running_avg = 0
    # times = 250
    # for i in range(times):
    #     running_avg += mean(net.weights)
    # print('avg', running_avg / times)
    net = network(100)
    print('generated', net)
    # animate_network(net)
    net.run_n_steps(10000)
    print('final', net)
    plot_contagion(net)

    # closeness = closeness_centrality(net.network_plot)
    # close_list = dict_to_list(closeness)
    # net.calculate_weights()
    # plot_network(net.network_plot, net.weights)
