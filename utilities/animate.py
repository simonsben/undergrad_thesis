from matplotlib.pylab import figure, show, savefig, title, axis, draw
from networkx import spring_layout, draw_networkx_edges, draw_networkx_nodes
from matplotlib.animation import FuncAnimation


def add_node(graph, i, plot_layout):
    # draw_networkx_edges(graph, plot_layout, alpha=.3)
    # draw_networkx_nodes(node, plot_layout, node_size=100, edgecolors='k', node_color='w')
    i += 1
    draw()


def animate_creation(network, blocking=True, save_plot=True):
    _title = 'Free-Scale Network'
    fig = figure(_title)
    axis('off')

    graph = network.network_plot
    plot_layout = spring_layout(graph)

    init_nodes = graph.nodes[:3]
    init_edges = graph.edges[:2]
    draw_networkx_nodes(graph, plot_layout, nodelist=init_nodes, node_size=100, edgecolors='k', node_color='w')
    draw_networkx_edges(graph, plot_layout, edgelist=init_edges, alpha=.3)
    draw()
    show()
    i = 3

    animation = FuncAnimation(fig, add_node, fargs=(graph, i, plot_layout))

