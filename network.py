from plot import generate_plot_network, plot_network
from utilities import balls_per_node
from polya_node import polya_node
from random import randint
from polya import run_polya


class network:
    def __init__(self, n):
        self.network_plot = generate_plot_network(n)
        self.nodes = []
        self.weights = []
        self.contagion = []
        self.steps = 1

        self.generate_network()
        self.calculate_weights()

    def calculate_weights(self):
        if len(self.weights) == 0 or len(self.weights) != len(self.nodes):
            self.weights = [0] * len(self.nodes)

        for i in range(len(self.weights)):
            self.weights[i] = self.nodes[i].weight

    def generate_network(self):
        # Generate nodes
        for node in self.network_plot:  # For each node in plot network
            # Randomize initial number of balls
            # TODO Ensure the distribution of the default random functions are sufficient
            num_red = randint(1, balls_per_node)
            num_black = balls_per_node - num_red

            new_node = polya_node(num_red, num_black, node)  # Create new node
            self.nodes.append(new_node)  # Add new node to network

        # Give each node a pointer to its neighbours
        for node in self.network_plot:  # For each node
            for neighbor in self.network_plot.neighbors(node):  # For each neighbour
                self.nodes[node].add_neighbour(self.nodes[neighbor])  # Add neighbour

    def calculate_contagion(self):
        running_avg, total_balls = 0, 0     # Initialize counting variables

        for node in self.nodes: # For each node
            total_balls += node.red + node.black    # Sum total balls
            running_avg += node.weight * (node.red + node.black)    # Sum weighted average

        avg_contagion = running_avg / total_balls
        self.contagion.append(avg_contagion)    # Add average at time n to list

    def run_step(self):
        self.nodes = run_polya(self.nodes, self.steps)
        self.steps += 1
        self.calculate_weights()
        self.calculate_contagion()

    def run_n_steps(self, n):
        for i in range(n):
            self.run_step()
            print('Done step ' + str(i))

    def plot_network(self):
        plot_network(self.network_plot, self.weights)

    def __str__(self):
        output = 'Network: '
        for node in self.nodes:
            output += str(node) + ' '
        return output
