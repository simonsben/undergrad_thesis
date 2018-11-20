from utilities.utilities import calculate_budget
from numpy import mean, argmin
from copy import deepcopy
from utilities.utilities import min_steps, min_trials


def optimize_starting(network):
    budget = calculate_budget(network.n)
    for i in range(budget):
        network = optimize_ball(network)
        print('Ball', (i+1), 'done', round((i+1) / budget * 100, 2), '% complete')
        # print(network)

    return network


def optimize_ball(network):
    trials = []
    for i in range(len(network)):
        trials.append(run_test(network, i))

    min_index = argmin(trials)
    network.nodes[min_index].add_ball('b')

    return network


def run_test(network, node_id):
    exposure = []

    for i in range(min_trials):
        tmp_net = deepcopy(network)
        tmp_net.nodes[node_id].add_ball('b')

        tmp_net.run_n_steps(min_steps)
        exposure.append(tmp_net.exposure[len(network.exposure)-1])

    return mean(exposure)
