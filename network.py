from plot import generate_plot_network, plot_network
from utilities import max_init_balls
from polya_node import polya_node
from random import randint
from polya import run_polya


class network:
    def __init__(self, n):
        self.network_plot = generate_plot_network(n)
        self.nodes = []
        self.weights = []
        self.steps = 1

        self.generate_network()
        self.calculate_weights()

    def calculate_weights(self):
        for node in self.nodes:
            self.weights.append(node.weight)

    def generate_network(self):
        # Generate nodes
        for node in self.network_plot:  # For each node in plot network
            # Randomize initial number of balls
            num_red = randint(1, max_init_balls)
            num_black = randint(1, max_init_balls)

            new_node = polya_node(num_red, num_black, node) # Create new node
            self.nodes.append(new_node) # Add new node to network

        # Give each node a pointer to its neighbours
        for node in self.network_plot:  # For each node
            for neighbor in self.network_plot.neighbors(node):  # For each neighbour
                self.nodes[node].add_neighbour(self.nodes[neighbor])    # Add neighbour

    def run_step(self):
        self.nodes = run_polya(self.nodes)
        self.steps += 1

    def plot_network(self):
        plot_network(self.network_plot, self.weights, self.steps)
