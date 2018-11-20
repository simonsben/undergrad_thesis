from csv import writer, reader
from networkx import to_numpy_array
from numpy import array

network_path = '../data/network.csv'
state_path = '../data/state.csv'


def save_network(network, network_file=network_path):
    adjacency = to_numpy_array(network)
    with open(network_file, 'w+', newline='') as fl:
        wtr = writer(fl)

        for row in adjacency:
            wtr.writerow(row)


def load_network(network_file=network_path):
    with open(network_file, 'r') as fl:
        rd = reader(fl)
        data = []

        for row in rd:
            data.append(row)

    return array(data)
