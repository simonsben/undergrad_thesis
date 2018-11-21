from typing import List
from utilities.plot import plot_network
from utilities.utilities import balls_per_node, balls_added, generate_plot_network, calculate_exposure
from model.polya_node import polya_node
from numpy import mean, zeros
from utilities.io import save_network
from random import random


class network:
    nodes: List[polya_node]

    def __init__(self, n, fix_start=True):
        self.network_plot = generate_plot_network(n)
        self.nodes = []
        self.weights = []
        self.contagion = []
        self.exposures = []
        self.node_exposures = zeros(n)

        self.n = n
        self.steps = 0
        self.current = 0

        self.generate_network(fix_start)
        self.calculate_exposure()

    def generate_network(self, fix_start):
        for i, node in enumerate(self.network_plot):
            if fix_start:
                new_node = polya_node(balls_per_node, balls_per_node, i)
            else:
                # TODO implement this case
                raise ValueError('Havent implemented this yet...')

            self.nodes.append(new_node)

        for i, node in enumerate(self.nodes):
            neighbour_indexes = [ind for ind in self.network_plot.neighbors(i)]
            self.nodes[i].add_neighbours([self.nodes[ind] for ind in neighbour_indexes])

    def calculate_exposure(self):
        return calculate_exposure(self)

    def run_step(self):
        picked_balls = zeros(self.n)
        for i in range(self.n):
            picked_balls[i] = 0 if random() < self.node_exposures[i] else 1

        for i, node in enumerate(self.nodes):
            node.add_ball(picked_balls[i])

        self.steps += 1
        self.calculate_exposure()

    def run_n_steps(self, n):
        for i in range(n):
            self.run_step()

    def plot_network(self):
        plot_network(self.network_plot, self.weights)

    def export_network(self):
        save_network(self.network_plot)

    # Utility function for starting iteration
    def __iter__(self):
        self.current = 0
        return self

    # Utility function for facilitating iteration on object
    def __next__(self):
        self.current += 1
        if self.current >= self.n:
            return StopIteration
        return self.nodes[self.current]

    def __len__(self):
        return len(self.nodes)

    # Utility function to return string of object for debugging
    def __str__(self):
        output = 'Network: '
        for node in self.nodes:
            output += str(node) + ' '
        return output
