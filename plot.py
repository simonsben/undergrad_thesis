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

    plt.figure(id)  # Make figure
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off') # Disable axis
    plt.show()  # Open matplotlib window


def run_update(tmp, network, layout):
    network.run_step()  # Run one polya step
    graph = network.network_plot    # Get pointer to network graph

    plt.cla()   # Clear figure

    plt.title('Network after ' + str(network.steps) + ' steps') # Add title to figure

    # TODO Display colormap legend
    nx.draw_networkx_edges(graph, layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, layout, node_size=80, node_color=network.weights, cmap=plt.cm.cool)   # Plot nodes


def animate_network(network):
    figure = plt.figure('Network animation')    # Initialize figure
    layout = nx.spring_layout(network.network_plot)     # Generate layout

    an = animation.FuncAnimation(figure, run_update, fargs=(network, layout), interval=250)  # Run animation

    plt.show()  # Show window
