from networkx import spring_layout, draw_networkx_nodes, draw_networkx_edges, kamada_kawai_layout, rescale_layout
from matplotlib.pyplot import figure, draw, axis, show, savefig, cm
from utilities import fig_size
from numpy import min, max, array


# Plot network
def plot_network(network, blocking=True, netx_plot=False, size=fig_size, weights=None, file_name=None, plot_edges=False, alph=.05):
    fig = figure(figsize=size)
    ax = fig.gca()
    ax.axis('off')  # Disable axis

    graph = network if netx_plot else network.network_plot
    plot_layout = kamada_kawai_layout(graph)

    sizes, edge_colors, node_colors = 80, 'k', 'w'
    if weights is not None:
        sizes = [50 if weight == 0 else 80 for weight in weights]
        node_colors = weights

    if plot_edges: draw_networkx_edges(graph, plot_layout, alpha=alph)
    draw_networkx_nodes(graph, plot_layout, node_size=sizes, linewidths=.5, edgecolors='k', node_color=node_colors,
                        cmap=cm.get_cmap('coolwarm'))
    draw()

    if file_name is not None: savefig(file_name, bbox_inches='tight', pad_inches=0)
    show(block=blocking)  # Open matplotlib window


# Plot airfield locations
def plot_net_w_routes(nodes, edges, plot_edges=True, blocking=True, file_name=None, single=-1, weights=None):
    fig = figure(figsize=fig_size)
    ax = fig.gca()
    ax.axis('off')

    if weights is None:
        colour = 'r' if single is None else 'k'
        ax.scatter(nodes[:, 2], nodes[:, 1], c=colour, s=5)  # Plot airports

        if single is not None and single > -1:
            ax.scatter(nodes[single, 2], nodes[single, 1], c='r', s=25)  # Plot airports
    else:
        cmap = cm.get_cmap('Blues')
        min_val = min(weights)
        max_val = max(weights)

        sizes = [10 if weight == 0 else 25 for weight in weights]
        plot_data = [[node[2], node[1], weights[i], sizes[i]] for i, node in enumerate(nodes)]
        plot_data = sorted(plot_data, key=lambda k: k[2])
        sizes = [data[3] for data in plot_data]

        plot_data = array(plot_data)[:, :3].astype(float)

        ax.scatter(plot_data[:, 0], plot_data[:, 1], c=plot_data[:, 2], vmin=min_val, vmax=max_val, cmap=cmap, s=sizes,
                   linewidths=.5, edgecolor='k')

    if plot_edges:
        for _, (src, dest) in enumerate(edges):  # Plot routes
            if type(src) is not list:
                src = nodes[src, 1:]
                dest = nodes[dest, 1:]
            ax.plot((src[1], dest[1]), (src[0], dest[0]), 'k', alpha=.1)

    if file_name is not None:
        try:
            savefig(file_name, bbox_inches='tight', pad_inches=0)
        except:
            print('Bad save!')

    if blocking:
        show()
