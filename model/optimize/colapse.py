from networkx import find_cliques, contracted_nodes, degree, generate_edgelist


def check_nodes(affected, clique):
    if len(clique) <= 3:
        return False
    for node in clique:
        if node in affected:
            return False
    return True


def simplify_net(network, netx_inp=False):
    netx = network.network_plot if not netx_inp else network
    degrees = degree(netx)

    while True:
        action = False
        affected_nodes = set()
        cliques = sorted(find_cliques(netx), key=lambda c: len(c), reverse=True)

        if len(cliques) <= 1:    # If no more cliques, break
            break

        # For each clique
        for i, clique in enumerate(cliques):
            clean_clique = check_nodes(affected_nodes, clique)

            if not clean_clique:    # If not clean, pass
                continue

            # Contract nodes
            action = True
            base = clique[0]
            affected_nodes.add(base)
            for j in range(1, len(clique)):
                netx = contracted_nodes(netx, base, clique[j])
                affected_nodes.add(clique[j])

        if not action:  # If not action in the last pass, done
            break

    return netx
