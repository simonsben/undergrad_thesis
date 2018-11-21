from model.network import network
from model.optimize import optimize_initial

net = network(100)
print('Network generated')
net.plot_network(1)


optimize_initial(net)
print('Optimization done.')
net.plot_network(2)
