import networkx as nx
import matplotlib.pyplot as plt


# Generate new network
def generate_plot_network(n):
    return nx.barabasi_albert_graph(n, 1)


# Plot network
def plot_network(graph, weights, id=0):
    layout = nx.spring_layout(graph)    # Calculate layout for nodes
    nx.draw_networkx_edges(graph, layout, alpha=.3) # Plot edges
    nx.draw_networkx_nodes(graph, layout, node_size=100, node_color=weights, cmap=plt.cm.cool)  # Plot nodes

    plt.figure(id)
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off') # Disable axis
    plt.show()  # Open matplotlib window
