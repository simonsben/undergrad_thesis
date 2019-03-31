from networkx import number_of_nodes
from utilities import dict_to_arr, balls_per_node, metrics, metric_names
from numpy import zeros, sum, argmax, array, take


def simple_centrality(network, method=0, netx_inp=False, red=None, budget_ratio=1, quiet=False, node_restriction=-1):
    metric = metrics.get(method)
    if metric is None:
        raise ValueError('Method value out of range')

    netx = network.network_plot if not netx_inp else network
    N = len(network) if not netx_inp else number_of_nodes(network)
    budget = int(balls_per_node * N * budget_ratio)

    centralities = dict_to_arr(metric(netx), conv=False)
    raw_centralities = array(sorted(centralities, key=lambda c: c[0]))
    centralities = raw_centralities[:, 1]
    cent_order = array(sorted(raw_centralities, key=lambda c: c[1], reverse=True))[:, 0]
    if node_restriction != -1: cent_order = cent_order[:node_restriction].astype(int)
    cent_total = sum(centralities) if node_restriction == -1 else sum(take(centralities, cent_order))

    black = zeros(N)
    for i in cent_order:
        ind = int(i)
        black[ind] = round(budget * centralities[ind] / cent_total)

    black_total = sum(black)
    if sum(black) <= budget: black[argmax(centralities)] += budget - black_total

    print(sum(black), sum(red))
    if not netx_inp: network.set_initial_distribution(red, black)
    if not quiet: print(metric_names[method] + ' with ' + str(budget_ratio) + ' ratio complete')
