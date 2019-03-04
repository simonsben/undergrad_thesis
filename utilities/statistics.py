from networkx import closeness_centrality, degree
from numpy import zeros, histogram


def degree_distribution(network):
    raw_degree = degree(network)
    node_degree = zeros(len(raw_degree), dtype=int)

    for i, node in enumerate(raw_degree):
        node_degree[i] = node[1]

    return node_degree


def degree_frequency(source, net_source=False):
    node_degree = source if not net_source else degree_distribution(source)
    return histogram(node_degree)


def centrality_distribution(network):
    return closeness_centrality(network.network_plot)

