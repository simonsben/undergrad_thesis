# Import libraries
from random import random
import networkx as nx
import matplotlib.pyplot as plt


def evaluate_probability(probability):
    return random() <= probability


# Generate new network
def generate_network(n):
    network = nx.barabasi_albert_graph(n, 1)
    initial_weights = [.5] * n
    return network, initial_weights


# Plot network
def plot_network(graph):
    nx.draw(graph)
    plt.draw()
    plt.show()
