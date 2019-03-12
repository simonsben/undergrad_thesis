from utilities import balls_per_node, dict_to_tuples, metrics, metric_names
from numpy import zeros


def maximum_entropy(network, netx_graph=False, metric_id=0):
    netx = network.network_plot if not netx_graph else network
    N = len(network)
    budget = balls_per_node * N

    # Calculate and sort centrality
    metric = metrics.get(metric_id)
    if metric is None: raise ValueError('Bad metric id')

    centralities = dict_to_tuples(metric(netx))
    centralities = sorted(centralities, key=lambda c: c[1], reverse=True)

    # Generate list of node neighbours
    neighbourhoods = [[neigh.id for neigh in node] for node in network.nodes]
    ball_counts = zeros((N, 2))
    ball_allocations = []

    # Super-urn ball counts
    for i, node in enumerate(network.nodes):
        ball_counts[i] = (node.red, 0)

        for neigh in neighbourhoods[i]:
            ball_counts[i, 0] += network.nodes[neigh].red

    # Place black in super urns
    for (ind, _) in centralities:
        tmp = ball_counts[ind, 0] - ball_counts[ind, 1]
        if tmp <= 0:
            continue
        num_added = tmp if budget > tmp else budget
        budget -= num_added

        ball_allocations.append((ind, num_added))

        ball_counts[ind, 1] += num_added
        for neigh in neighbourhoods[ind]:
            ball_counts[neigh, 1] += num_added

        if budget == 0:
            break

    # Distribute remainder of balls
    if budget > 0:
        max_ind = centralities[0][0]
        ball_counts[max_ind, 1] += budget
        ball_allocations[0][1] += budget

        for neigh in neighbourhoods[max_ind]:
            ball_counts[neigh, 1] += budget

    black_dist = zeros(N)
    for (ind, alloc) in ball_allocations:
        black_dist[ind] = alloc

    network.set_initial_distribution(black=black_dist)

    print('Maximum entropy strategy with ' + metric_names[metric_id] + ' complete')
