from model.network import network
from numpy import copy
from utilities.plot import plot_exposures, plot_degree_frequency


net = network(100)
print('Network generated')

num_steps = 250
num_trials = 30
default_set = []
gradient_set = []
heuristic_set = []

net.plot_network(1)

for i in range(num_trials):
    net.run_n_steps(num_steps)
    default_set.append(copy(net.exposures))
    net.clear_network()
print('Default Complete')

net.optimize_initial()
net.plot_network(2, False)
for i in range(num_trials):
    net.run_n_steps(num_steps)
    gradient_set.append(copy(net.exposures))
    net.clear_network()
print('Gradient complete')

net.reset_network()
net.optimize_initial(gradient=False)
for i in range(num_trials):
    net.run_n_steps(num_steps)
    heuristic_set.append(copy(net.exposures))
    net.clear_network()
print('Heuristic complete')

plot_degree_frequency(net)
plot_exposures(default_set, gradient_set, heuristic_set)
