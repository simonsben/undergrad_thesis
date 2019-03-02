from model.network import network
from numpy import copy

net = network(100)
print('Network generated')

num_steps = 250
num_trials = 30
default_set = []
gradient_set = []
heuristic_set = []
random_set = []

net.plot_network(1)
for i in range(num_trials):
    net.run_n_steps(num_steps)
    default_set.append(copy(net.exposures))
    net.clear_network()
print('Default Complete')

net.optimize_initial(method=0)
net.plot_network(2, True)
# for i in range(num_trials):
#     net.run_n_steps(num_steps)
#     gradient_set.append(copy(net.exposures))
#     net.clear_network()
# print('Gradient complete')
#
# net.reset_network()
# net.optimize_initial(method=1)
# for i in range(num_trials):
#     net.run_n_steps(num_steps)
#     heuristic_set.append(copy(net.exposures))
#     net.clear_network()
# print('Heuristic complete')
#
#
# net.reset_network()
# net.optimize_initial(method=2)
# for i in range(num_trials):
#     net.run_n_steps(num_steps)
#     random_set.append(copy(net.exposures))
#     net.clear_network()
# print('Random complete')
#
#
# plot_degree_frequency(net)
# plot_infection(default_set, gradient_set, heuristic_set, random_set)
