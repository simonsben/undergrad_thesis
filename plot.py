import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation

plot_layout = None  # Only define layout once

# Generate new network
def generate_plot_network(n):
    return nx.barabasi_albert_graph(n, 1)


# Plot network
def plot_network(graph, weights, id=1):
    global plot_layout
    if not plot_layout: # If first plot
        plot_layout = nx.spring_layout(graph)    # Calculate layout for nodes
    nx.draw_networkx_edges(graph, plot_layout, alpha=.3) # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=weights, cmap=plt.cm.cool)  # Plot nodes

    plt.figure(id)
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off') # Disable axis
    plt.show()  # Open matplotlib window


def run_network_update(tmp, network, plot_layout):
    graph = network.network_plot
    network.run_step()
    nx.draw_networkx_edges(graph, plot_layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=network.weights, cmap=plt.cm.cool)  # Plot nodes

# animate network
def animate_network(network, n):
    figure = plt.figure('test figure')
    plt.axis('off') # Disable axis

    plot_layout = network.network_plot

    # plot_layout = nx.spring_layout(graph)    # Generate layout
    # nx.draw_networkx_edges(graph, plot_layout, alpha=.3) # Plot edges
    # nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=network.weights, cmap=plt.cm.cool)  # Plot nodes

    network_animation = animation.ArtistAnimation(figure, run_network_update, fargs=(network, plot_layout), interval=10)

    plt.show()  # Open matplotlib window
