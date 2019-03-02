from model.network import network
from utilities.plotting import plot_degree_frequency

net = network(15)
print('Network generated')
net.plot_network(1)


net.optimize_initial()
net.lock_optimization()
print('Optimization done.')
plot_degree_frequency(net)
net.plot_network(2)
