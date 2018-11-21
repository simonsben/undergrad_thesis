from model.network import network
from model.optimize import optimize_initial
from utilities.plot import plot_optimized_network

net = network(100)
print('Network generated')
plot_optimized_network(net, 1, blocking=False)


optimize_initial(net)
print('Optimization done.')
plot_optimized_network(net, 2)
