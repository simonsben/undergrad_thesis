import networkx as nx
from matplotlib.pyplot import figure, draw, axis, show, cm, colorbar, Normalize, subplot, title, savefig
# from matplotlib import animation
# from utilities.utilities import min_steps
# from copy import deepcopy
from numpy import min, max


# Plot network
def plot_optimized_network(network, index, blocking=True, save_plot=True):
    _title = 'Network plot'

    network.calculate_weights()
    graph = network.network_plot
    weights = network.weights

    if index == 1:
        figure(_title)
    subplot(2, 1, index)

    if index == 1:
        title('Initial network')
    else:
        title('Optimized network')

    cmap = cm.cool
    color_vals = cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=min(weights), vmax=max(weights)))
    color_vals._A = []

    plot_layout = nx.spring_layout(graph)  # Calculate layout for nodes
    nx.draw_networkx_edges(graph, plot_layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, edgecolors='k', node_color=network.weights, cmap=cm.cool)

    draw()  # Matplotlib virtual draw
    colorbar(color_vals)
    axis('off')  # Disable axis

    if save_plot and index == 2:
        savefig('../results/optimized_network.png')
    show(block=blocking)  # Open matplotlib window


# def run_update(tmp, network, layout):
#     network.run_step()  # Run one polya step
#     graph = network.network_plot  # Get pointer to network graph
#
#     plt.cla()  # Clear figure
#
#     plt.title('Network after ' + str(network.steps) + ' steps')  # Add title to figure
#
#     nx.draw_networkx_edges(graph, layout, alpha=.3)  # Plot edges
#     nx.draw_networkx_nodes(graph, layout, node_size=80, node_color=network.weights, cmap=plt.cm.cool)  # Plot nodes
#
#
# def plot_contagion(network):
#     plt.figure('Network contagion over time')
#     plt.plot(network.contagion)
#     plt.title('Network contagion over ' + str(network.steps) + ' steps')
#     plt.show()
#
#
# def run_and_plot_exposure(network, num_runs=4):
#     run_exposures = []
#     for i in range(num_runs):
#         tmp_net = deepcopy(network)
#         tmp_net.run_n_steps(2000)
#
#         run_exposures.append(tmp_net.exposure)
#
#     average_exp = mean(run_exposures, 0)
#     plt.figure('Exposure over ' + str(min_steps) + 'steps')
#
#     for i in range(num_runs):
#         plt.plot(run_exposures[i], label='Run ' + str(i))
#     plt.plot(average_exp, label='Average')
#     plt.legend(loc='right')
#     plt.show()
#
#
# def animate_network(network):
#     figure = plt.figure('Network animation')  # Initialize figure
#     layout = nx.spring_layout(network.network_plot)  # Generate layout
#
#     # Run animation
#     an = animation.FuncAnimation(figure, run_update, fargs=(network, layout), interval=250, frames=10, repeat=False)
#
#     plt.show()  # Show window
