from networkx import number_of_nodes
from utilities import dict_to_arr, balls_per_node, metrics, metric_names
from numpy import zeros, sum, argmax


def simple_centrality(network, method=0, netx_inp=False, red=None, budget_ratio=1):
    metric = metrics.get(method)
    if metric is None:
        raise ValueError('Method value out of range')

    netx = network.network_plot if not netx_inp else network
    N = len(network) if not netx_inp else number_of_nodes(network)
    budget = int(balls_per_node * N * budget_ratio)

    centralities = dict_to_arr(metric(netx), conv=False)
    cent_total = sum(centralities)

    black = zeros(N)
    for i in range(N):
        black[i] = round(budget * centralities[i] / cent_total)

    black_total = sum(black)
    if sum(black) <= budget:
        black[argmax(centralities)] += budget - black_total

    network.set_initial_distribution(red, black)
    print(metric_names[method] + ' with ' + str(budget_ratio) + ' ratio complete')
