from utilities import calculate_budget
from numpy import mean, argmin
from copy import deepcopy

min_steps = 10000
min_trials = 10


def optimize_starting(network):
    budget = calculate_budget(network.n)
    for i in range(budget):
        network = optimize_ball(network)
        print('Ball', (i+1), 'done', round((i+1) / budget * 10, 2), '% complete')

    print(network)
    return network


def optimize_ball(network):
    trials = []
    networks = []
    for i in range(len(network)):
        tmp_net = deepcopy(network)
        networks.append(tmp_net)
        tmp_net.nodes[i].add_ball('b')
        trials.append(run_test(tmp_net))

    min_index = argmin(trials)
    return networks[min_index]


def run_test(network):
    contagion = []
    for i in range(min_trials):
        network.run_n_steps(min_steps)
        contagion.append(network.contagion[len(network.contagion)-1])

    return mean(contagion)
