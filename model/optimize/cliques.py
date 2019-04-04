from networkx import find_cliques, number_of_nodes, degree
from numpy import zeros, array, sum, take, argmax
from utilities import metrics, dict_to_arr


def simple_cliques(net, num_cliques, budget, netx_plot=False, cliques=None, single_place=False):
    netx = net if netx_plot else net.network_plot

    # Pre-requisite calculations
    if cliques is None: cliques = sorted(find_cliques(netx), key=lambda c: len(c), reverse=True)
    N = number_of_nodes(netx)
    if single_place:
        degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]

    # Get clique total to allocate over
    total_nodes = 0
    for i in range(num_cliques): total_nodes += len(cliques[i])

    # Allocate balls
    B = zeros(N)
    for i in range(num_cliques):
        clique_budget = len(cliques[i]) / total_nodes * budget

        if not single_place:
            per_node = clique_budget / len(cliques[i])
            for ind in cliques[i]:
                B[ind] += round(per_node)
        else:
            clique_degrees = take(degrees, cliques[i])
            rel_max = argmax(clique_degrees)
            B[rel_max] += round(clique_budget)

    print(sum(B))

    if not netx_plot: net.set_initial_distribution(black=B)
    else: return B


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

    return weights, cliques, node_weights


def weighted_cliques(net, num_cliques, budget, netx_plot=False, metric_id=2, data=None):
    netx = net if netx_plot else net.network_plot
    if data is None:
        weights, cliques, node_weights = calculate_clique_weights(net, metric_id=metric_id)
    else:
        weights, cliques, node_weights = data
    N = number_of_nodes(netx)

    # Calculate total weight
    total_weight = 0
    for i in range(num_cliques): total_weight += weights[i, 1]

    # Allocate balls
    B = zeros(N)
    for i in range(num_cliques):
        ind = int(round(weights[i, 0]))
        clique_budget = weights[i, 1] / total_weight * budget
        clique_node_weights = take(node_weights, cliques[ind])

        max_rel_ind = argmax(clique_node_weights)
        ind = cliques[ind][max_rel_ind]

        B[ind] += round(clique_budget)

    print(sum(B))


def popularity_contest(net, num_cliques, budget):
    netx = net.network_plot
    N = number_of_nodes(netx)
    print('Num cliques: ' + str(num_cliques))

    cliques = sorted(find_cliques(netx), key=lambda c: len(c), reverse=True)

    popular = {}
    for i in range(num_cliques):
        clique = cliques[i]
        for ind in clique:
            if ind in popular:
                popular[ind] += 1
            else:
                popular[ind] = 1
    popular = [[ind, popular[ind]] for ind in popular]
    popular = sorted(popular, key=lambda p: p[1], reverse=True)

    total = 0
    for pop in popular:
        if pop[1] > 1: total += pop[1]

    B = zeros(N)
    for pop in popular:
        if pop[1] > 1:
            B[pop[0]] += round(pop[1] / total * budget)

    print(sum(B))

    net.set_initial_distribution(black=B)
