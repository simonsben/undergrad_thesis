from model.network import network
from numpy import copy
from utilities.plot import plot_exposures


net = network(100)
print('Network generated')

num_steps = 500
num_trials = 15
default_set = []
optimized_set = []

net.plot_network(1)

for i in range(num_trials):
    net.run_n_steps(num_steps)
    default_set.append(copy(net.exposures))
    net.clear_network()


net.optimize_initial()
net.plot_network(2, False)
for i in range(num_trials):
    net.run_n_steps(num_steps)
    optimized_set.append(copy(net.exposures))
    net.clear_network()


plot_exposures(default_set, optimized_set)
