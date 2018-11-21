from utilities.utilities import get_node


def optimize_initial(network):
    current_exposure = network.exposures[len(network.exposures)-1]

    while True:
        min_node, _, urn_counts = get_node(network, False)

        if network.nodes[min_node] - 1 < 0:
            print('Negative value,  breaking.')
            break
        network.nodes[min_node] -= 1

        max_node, new_exposure, _ = get_node(network, True, urn_counts)

        if new_exposure < current_exposure:
            print('Worsened exposure, breaking.')
            break

        network.nodes[max_node] += 1
        current_exposure = new_exposure

    print('Optimization done')
    print(network)
