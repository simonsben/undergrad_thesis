from model.network import network
from model.optimize import optimize_initial
from utilities.plot import plot_network

net = network(5)
print('Network generated')
plot_network(net, 'initial', blocking=False)


optimize_initial(net)
print('Optimization done.')
print(net)
plot_network(net)
