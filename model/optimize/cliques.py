from networkx import find_cliques, number_of_nodes
from numpy import zeros, array, sum
from utilities import metrics, dict_to_arr


def simple_cliques(net, num_cliques, budget, netx_plot=False, cliques=None):
    netx = net if netx_plot else net.network_plot

    # Pre-requisite calculations
    if cliques is None: cliques = sorted(find_cliques(netx), key=lambda c: len(c), reverse=True)
    N = number_of_nodes(netx)

    # Get clique total to allocate over
    total_nodes = 0
    for i in range(num_cliques): total_nodes += len(cliques[i])

    # Allocate balls
    B = zeros(N)
    for i in range(num_cliques):
        prop = len(cliques[i]) / total_nodes
        per_node = prop / len(cliques[i]) * budget
        for ind in cliques[i]:
            B[ind] += per_node

    if not netx_plot:
        net.set_initial_distribution(black=B)
    else:
        return B


def calculate_clique_weights(net, netx_plot=False, metric_id=2):
    netx = net if netx_plot else net.network_plot
    cliques = [clique for clique in find_cliques(netx)]

    node_weights = dict_to_arr(metrics[metric_id](netx))

    # Calculate clique weights
    weights = []
    for i, clique in enumerate(cliques):
        weights.append([i, 0])
        for ind in clique:
            weights[i][1] += node_weights[ind]
    weights = array(sorted(weights, key=lambda w: w[1], reverse=True))

    return weights, cliques


def weighted_cliques(net, num_cliques, budget, netx_plot=False, metric_id=2, data=None):
    netx = net if netx_plot else net.network_plot
    if data is None:
        weights, cliques = calculate_clique_weights(net, metric_id=metric_id)
    else:
        weights, cliques = data
    N = number_of_nodes(netx)

    # Calculate total weight
    total_weight = 0
    for i in range(num_cliques): total_weight += weights[i, 1]

    # Allocate balls
    B = zeros(N)
    for i in range(num_cliques):
        ind = int(round(weights[i, 0]))
        per_node = weights[i, 1] / (total_weight * len(cliques[ind])) * budget
        for node in cliques[ind]:
            B[node] += per_node

    print(sum(B))

