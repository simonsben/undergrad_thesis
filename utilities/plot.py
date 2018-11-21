from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges
from matplotlib.pyplot import figure, draw, axis, show, cm, colorbar, Normalize, subplot, title, savefig, plot


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


def plot_exposures(exposure_set):
    num_steps = str(len(exposure_set[0]))
    _title = 'Network exposure over ' + num_steps + ' steps'

    figure('Exposure')
    for exposures in exposure_set:
        plot(exposures)
    savefig('../results/network_exposure_' + num_steps + '.png')
    show()


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
