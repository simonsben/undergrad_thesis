from matplotlib.pyplot import figure, show, title, savefig, plot, legend, scatter, xlabel, ylabel
from numpy import array, polyfit, poly1d, linspace, zeros
from utilities.io import save_frequencies


# TODO generalize function
def plot_degree_frequency(network, _title='Fraction of Nodes with Difference Degree', blocking=False, save=True):
    frequencies = {}
    for node in network.nodes:
        degree = node.degree
        if degree in frequencies:
            frequencies[degree] += 1
        else:
            frequencies[degree] = 1

    n = network.n
    t_frequencies = array([(degree, frequencies[degree] / n) for degree in frequencies])

    figure(_title)
    scatter(t_frequencies[:, 0], t_frequencies[:, 1])
    title(_title)
    xlabel('Node Degree')
    ylabel('Fraction of Nodes')

    if save:
        savefig('../../results/degree_frequencies.png')
        save_frequencies(t_frequencies)

    show(block=blocking)


def plot_w_best_fit(data, _title='Fitted data', filename='', blocking=False, x_label='', y_label='', data_name='', degree=2):
    figure(_title)
    x, y = data[:, 0], data[:, 1]
    plot(x, y, '.k', label='Execution times')

    domain = linspace(min(x), max(x))
    plot(domain, poly1d(polyfit(x, y, degree))(domain), label='Line of best fit')
    legend()

    title(_title)
    xlabel(x_label)
    ylabel(y_label)

    if filename != '':
        savefig(filename)
    if data_name != '':
        save_frequencies(data, data_name)

    show(block=blocking)


def plot_weight_delta(network, save=True, blocking=False):
    _title = 'Node weight differences'
    differences = zeros(network.n)

    for i, node in enumerate(network.nodes):
        differences[i] = network.weights[i] - network.init_weights[i]

    figure(_title)
    scatter(list(range(network.n)), differences, label='Residuals')
    legend()
    xlabel('Node')
    ylabel('Difference of red balls')
    title(_title)

    if save:
        filename = '../results/weight_delta_' + str(network.n) + '.png'
        savefig(filename)
    show(block=blocking)
