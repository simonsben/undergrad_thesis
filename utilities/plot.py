from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges
from matplotlib.pyplot import figure, draw, axis, show, cm, colorbar, Normalize, \
    subplot, title, savefig, plot, legend, scatter, xlabel, ylabel
from numpy import mean, array, polyfit, poly1d, linspace, zeros
from utilities.io import save_frequencies


# Plot network
def plot_optimized_network(network, blocking=True, save_plot=True):
    _title = 'Network plot'
    figure(_title)

    graph = network.network_plot
    init_weights = network.init_weights
    weights = network.weights
    plot_layout = spring_layout(graph)

    min_val = 0
    max_val = 1

    cmap = cm.bwr
    color_vals = cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=min_val, vmax=max_val))
    color_vals._A = []

    subplot(2, 1, 1)
    title('Initial network')
    colorbar(color_vals)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=100, edgecolors='k', node_color=init_weights, cmap=cmap,
                        vmin=min_val, vmax=max_val)
    axis('off')  # Disable axis

    subplot(2, 1, 2)
    title('Optimized network')
    colorbar(color_vals)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=100, edgecolors='k', node_color=weights, cmap=cmap,
                        vmin=min_val, vmax=max_val)
    axis('off')
    draw()

    if save_plot:
        savefig('../results/optimized_network.png')
    show(block=blocking)  # Open matplotlib window


def plot_exposures(default_set, optimized_set):
    num_steps = str(len(default_set[0]))
    _title = 'Network exposure over ' + num_steps + ' steps'

    figure('Exposure')
    for i, exposures in enumerate(default_set):
        plot(exposures, alpha=.3)

    for i, exposures in enumerate(optimized_set):
        plot(exposures, alpha=.3)

    plot(mean(default_set, axis=0), label='Uniform average')
    plot(mean(optimized_set, axis=0), label='Optimal average')

    legend()
    savefig('../results/network_exposure_' + num_steps + '.png')
    show()


# Plot network
def plot_network(network, blocking=True, save_plot=True, _title='Network plot'):
    figure(_title)
    title(_title)
    axis('off')  # Disable axis

    graph = network.network_plot
    plot_layout = spring_layout(graph)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=80, edgecolors='k', node_color='w')
    draw()

    if save_plot:
        savefig('../results/network_plot.png')
    show(block=blocking)  # Open matplotlib window


# TODO generalize function
def plot_degree_frequency(network, _title='Node Degree vs Degree Frequency', blocking=False, save=True):
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
    ylabel('Frequency')

    if save:
        savefig('../results/degree_frequencies.png')
        save_frequencies(t_frequencies)

    show(block=blocking)


def plot_w_best_fit(data, _title='Fitted data', filename='', blocking=False, x_label='', y_label='', data_name=''):
    figure(_title)
    x, y = data[:, 0], data[:, 1]
    plot(x, y, '.k', label='Execution times')

    domain = linspace(min(x), max(x))
    plot(domain, poly1d(polyfit(x, y, 2))(domain), label='Line of best fit')
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
