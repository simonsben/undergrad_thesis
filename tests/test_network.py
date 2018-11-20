from model.network import network
from networkx import to_numpy_array

net = network(15)
print(to_numpy_array(net.network_plot))

print(net)
print(net.exposures)

net.run_n_steps(10)
print(net)
print(net.exposures)

