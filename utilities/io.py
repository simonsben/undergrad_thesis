from csv import writer, reader
from networkx import to_numpy_array, from_numpy_array, from_edgelist
from numpy import array

network_path = '../data/network.csv'
state_path = '../data/state.csv'
frequency_path = '../data/execution_times.csv'
airport_path = '../data/source/airports.dat'
route_path = '../data/source/routes.dat'


def save_network(network, network_file=network_path):
    adjacency = to_numpy_array(network.network_plot)
    with open(network_file, 'w', newline='') as fl:
        wtr = writer(fl)

        for row in adjacency:
            wtr.writerow(row)


def load_network(network_file=network_path, edgelist=False):
    with open(network_file, 'r') as fl:
        rd = reader(fl)
        data = []

        for row in rd:
            data.append(row)

    if edgelist:
        return from_edgelist(data)
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


# Function to import specific columns of csv file
def load_csv_col(file, cols=None, np_arr=True, with_headers=False):
    data = []
    headers = None
    with open(file, encoding='utf8') as fl:
        fl_reader = reader(fl)
        if with_headers:
            headers = next(fl_reader)
        for _, line in enumerate(fl_reader):
            tmp = []
            try:
                if cols is not None:
                    for _, cl in enumerate(cols):
                        tmp.append(cl[1](line[cl[0]]))
                else:
                    tmp = line
                data.append(tmp)
            except ValueError:
                continue

    data = array(data) if np_arr else data
    if with_headers:
        return data, headers
    return data


def save_trials(trial_data, filename, titles=None):
    if type(trial_data) is not array:
        trial_data = array(trial_data)

    with open(filename, 'w', newline='') as fl:
        wtr = writer(fl)

        if titles is not None:
            wtr.writerow(titles)

        steps = len(trial_data[0])
        for i in range(steps):
            wtr.writerow(trial_data[:, i])


def save_distribution(dist, deep_save=False):
    path = '../data/optimal_distribution/analytical.csv'
    if deep_save:
        path = '../' + path

    with open(path, 'w', newline='') as fl:
        wtr = writer(fl)

        wtr.writerow(dist)
