# Import libraries
from random import random
import networkx as nx
import matplotlib.pyplot as plt

network_memory = 10000
balls_added = 1


def evaluate_probability(probability):
    return random() <= probability


# Generate new network
def generate_network(n):
    network = nx.barabasi_albert_graph(n, 1)
    initial_weights = [.5] * n
    return network, initial_weights


# Plot network
def plot_network(graph, weights):
    layout = nx.spring_layout(graph)    # Calculate layout for nodes
    nx.draw_networkx_edges(graph, layout, alpha=.3) # Plot edges
    nx.draw_networkx_nodes(graph, layout, node_size=100, node_color=weights, cmap=plt.cm.cool)  # Plot nodes
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off') # Disable axis
    plt.show()  # Open matplotlib window
