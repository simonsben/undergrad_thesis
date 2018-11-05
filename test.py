from network import network
# from plot import animate_network
from plot import plot_contagion

net = network(1000)
# animate_network(net)
net.run_n_steps(250)

plot_contagion(net)
