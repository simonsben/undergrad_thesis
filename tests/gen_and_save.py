from model.network import network
from utilities import save_network, load_network
from networkx import to_numpy_array

net = network(10)
print('net gen')
tmp_net = to_numpy_array(net.network_plot)
print(tmp_net)

save_network(net)
print('save done')

net_cpy = load_network()
print(to_numpy_array(net_cpy))
print('load done')
