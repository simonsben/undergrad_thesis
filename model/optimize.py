from utilities.utilities import get_node, increment_values


def optimize_initial(network):
    current_exposure = network.exposures[len(network.exposures)-1]

    while True:
        min_node, _, urn_counts = get_node(network, False)

        if network.nodes[min_node].red - 1 < 0:
            print('Negative value,  breaking.')
            break
        network.nodes[min_node].red -= 1
        network.nodes[min_node].init_total -= 1
        increment_values(min_node, network, urn_counts, -1)

        max_node, exposure_change, _ = get_node(network, True)

        # new_exposure = current_exposure +
        print('Change', exposure_change)
        if exposure_change <= 0 or min_node == max_node:
            print('Worsened exposure, breaking.')
            network.nodes[min_node].red += 1
            network.nodes[min_node].init_total += 1
            break

        increment_values(max_node, network, urn_counts, 1)
        network.nodes[max_node].red += 1
        network.nodes[max_node].init_total += 1
        current_exposure += exposure_change
        print(network)
