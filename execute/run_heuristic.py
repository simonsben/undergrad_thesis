from model.network import network
from utilities.plot import plot_weight_delta
from matplotlib.pylab import show


net = network(10)

net.optimize_initial(False, True)
net.plot_network(1)

net.optimize_initial(False, False)

net.plot_network(2, blocking=False)
plot_weight_delta(net)
show()
