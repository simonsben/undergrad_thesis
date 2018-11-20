from model.network import network
# from plot import animate_network
from utilities.plot import plot_contagion

if __name__ == '__main__':
    # running_avg = 0
    # times = 250
    # for i in range(times):
    #     running_avg += mean(net.weights)
    # print('avg', running_avg / times)
    net = network(3)
    print('generated', net)
    # animate_network(net)
    net.run_n_steps(10000)
    print('final', net)
    plot_contagion(net)

    # closeness = closeness_centrality(net.network_plot)
    # close_list = dict_to_list(closeness)
    # net.calculate_weights()
    # plot_network(net.network_plot, net.weights)
