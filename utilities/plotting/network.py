from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges
from matplotlib.pyplot import figure, draw, axis, show, title, savefig


# Plot network
def plot_network(network, blocking=True, save_plot=True, _title='Network plotting', netx_plot=False, size=(8, 5)):
    figure(_title, figsize=size)
    title(_title)
    axis('off')  # Disable axis

    graph = network if netx_plot else network.network_plot
    plot_layout = spring_layout(graph)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=80, edgecolors='k', node_color='w')
    draw()

    if save_plot:
        savefig('../results/network_plot.png')
    show(block=blocking)  # Open matplotlib window
