from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges
from matplotlib.pyplot import figure, draw, axis, show, cm, colorbar, Normalize, \
    title, savefig, subplot
from numpy import max as np_max


# Plot network
def plot_optimized_network(network, blocking=True, save_plot=True):
    _title = 'Optimized network vs. non-optimized'
    figure(_title)

    graph = network.network_plot
    plot_layout = spring_layout(graph)

    balls = network.get_ball_distribution()

    print(network.ref_distribution)
    print(balls)

    min_val = 0
    max_val = max([np_max(network.ref_distribution), np_max(balls)])

    cmap = cm.Greys
    color_vals = cm.ScalarMappable(cmap=cmap, norm=Normalize(vmin=min_val, vmax=max_val))
    color_vals._A = []

    subplot(2, 1, 1)
    title('Initial network')
    colorbar(color_vals)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=100, edgecolors='k',
                        node_color=network.ref_distribution, cmap=cmap, vmin=min_val, vmax=max_val)
    axis('off')  # Disable axis

    subplot(2, 1, 2)
    title('Optimized network')
    colorbar(color_vals)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=100, edgecolors='k',
                        node_color=balls, cmap=cmap, vmin=min_val, vmax=max_val)
    axis('off')
    draw()

    if save_plot:
        savefig('../results/optimized_network.png')
    show(block=blocking)  # Open matplotlib window
