from csv import writer, reader
from networkx import to_numpy_array, from_numpy_array
from numpy import array

network_path = '../data/network.csv'
state_path = '../data/state.csv'
frequency_path = '../data/execution_times.csv'


def save_network(network, network_file=network_path):
    adjacency = to_numpy_array(network.network_plot)
    with open(network_file, 'w', newline='') as fl:
        wtr = writer(fl)

        for row in adjacency:
            wtr.writerow(row)


def load_network(network_file=network_path):
    with open(network_file, 'r') as fl:
        rd = reader(fl)
        data = []

        for row in rd:
            data.append(row)

    return from_numpy_array(array(data))


def save_frequencies(frequencies, filename=frequency_path):
    with open(filename, 'w', newline='') as fl:
        wtr = writer(fl)

        for frequency in frequencies:
            wtr.writerow(frequency)


def load_frequencies(filename=frequency_path, cast=True):
    with open(filename, 'r') as fl:
        rd = reader(fl)
        data = []

        for row in rd:
            tmp_row = array(row).astype(float) if cast else row
            data.append(tmp_row)

    return array(data)
