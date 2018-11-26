from model.network import network
from model.optimize import optimize_initial
from utilities.plot import plot_degree_frequency

net = network(100)
print('Network generated')
net.plot_network(1)


optimize_initial(net)
print('Optimization done.')
plot_degree_frequency(net)
net.plot_network(2)
