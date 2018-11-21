from model.network import network
from model.optimize import optimize_initial

net = network(5)
print('Network generated')


optimize_initial(net)
print('Optimization done.')
print(net)
