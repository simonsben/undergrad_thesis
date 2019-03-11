from networkx import eigenvector_centrality, closeness_centrality, betweenness_centrality, \
    degree_centrality, number_of_nodes
from utilities import dict_to_arr, balls_per_node
from numpy import zeros

methods = {
    0: eigenvector_centrality,
    1: closeness_centrality,
    2: betweenness_centrality,
    3: degree_centrality
}

metric_names = [
    'Closeness centrality',
    'Eigenvector centrality',
    'Betweenness centrality',
    'Degree centrality'
]


def simple_centrality(network, method=0, netx_inp=False, red=None):
    metric = methods.get(method)
    if metric is None:
        raise ValueError('Method value out of range')

    netx = network.network_plot if not netx_inp else network
    N = len(network) if not netx_inp else number_of_nodes(network)
    budget = balls_per_node * N

    centralities = dict_to_arr(metric(netx), conv=False)
    cent_total = sum(centralities)

    black = zeros(N)
    for i in range(N):
        black[i] = round(budget * centralities[i] / cent_total)

    network.set_initial_distribution(red, black)
    print(metric_names[method] + ' complete')
