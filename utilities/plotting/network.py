from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges
from matplotlib.pyplot import figure, draw, axis, show, title, savefig
from utilities import fig_size


# Plot network
def plot_network(network, blocking=True, save_plot=True, netx_plot=False, size=fig_size):
    figure(figsize=size)
    axis('off')  # Disable axis

    graph = network if netx_plot else network.network_plot
    plot_layout = spring_layout(graph)

    draw_networkx_edges(graph, plot_layout, alpha=.3)
    draw_networkx_nodes(graph, plot_layout, node_size=80, edgecolors='k', node_color='w')
    draw()

    if save_plot:
        savefig('../results/network_plot.png')
    show(block=blocking)  # Open matplotlib window


# Plot airfield locations
def plot_net_w_routes(nodes, edges, fig_title='Network', plot_edges=True, blocking=True, file_name=None):
    fig = figure(fig_title, figsize=fig_size)
    ax = fig.gca()
    # ax.set_title(fig_title)
    ax.scatter(nodes[:, 2], nodes[:, 1], s=5)  # Plot airports
    if plot_edges:
        for _, (src, dest) in enumerate(edges):  # Plot routes
            if type(src) is not list:
                src = nodes[src, 1:]
                dest = nodes[dest, 1:]
            ax.plot((src[1], dest[1]), (src[0], dest[0]), 'k', alpha=.1)

    if file_name is not None:
        try:
            savefig(file_name)
        except: pass

    if blocking:
        show()
