from model.network import network
from utilities.io import save_network, load_network
from numpy import copy
from utilities.plot import plot_exposures


net = network(25)
save_network(net)
print('Network generated')
net.plot_network(1)

# net.run_n_steps(500)
# default_exposure = copy(net.exposures)

net.clear_network()
net.optimize_initial()
net.plot_network(2)

# plot_exposures([default_exposure, net.exposures])


