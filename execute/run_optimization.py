from model.network import network
from model.optimize import optimize_initial

net = network(3)
print('Network generated')

optimize_initial(net)

