import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation


# Generate new network
def generate_plot_network(n):
    return nx.barabasi_albert_graph(n, 1)


# Plot network
def plot_network(graph, weights, id=1):
    plot_layout = nx.spring_layout(graph)    # Calculate layout for nodes
    nx.draw_networkx_edges(graph, plot_layout, alpha=.3) # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=weights, cmap=plt.cm.cool)  # Plot nodes

    plt.figure(id)
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off') # Disable axis
    plt.show()  # Open matplotlib window


def run_update(tmp, network, layout):
    network.run_step()
    graph = network.network_plot

    plt.cla()

    nx.draw_networkx_edges(graph, layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, layout, node_size=100, node_color=network.weights, cmap=plt.cm.cool)


def animate_network(network):
    figure = plt.figure('Network animation')
    layout = nx.spring_layout(network.network_plot)

    network_animation = animation.FuncAnimation(figure, run_update, fargs=(network, layout), interval=250)

    plt.show()
