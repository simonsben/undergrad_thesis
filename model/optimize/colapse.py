from networkx import enumerate_all_cliques


def simplify_net(network, netx_inp=False):
    netx = network.network_plot if not netx_inp else network

    for cl in enumerate_all_cliques(netx):
        print(cl)

