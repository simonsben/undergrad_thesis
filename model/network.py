from typing import List
from utilities.plot import plot_network
from utilities.utilities import balls_per_node, balls_added, generate_plot_network
from model.polya_node import polya_node
from numpy import mean, sum
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
        self.node_exposures = []

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
        delta_balls = self.steps * balls_added
        ball_counts = [[node.red, node.init_total + delta_balls]
                       for node in self.nodes]

        urn_counts = [sum([ball_counts[node.id],
                           sum([ball_counts[neighbour.id] for neighbour in node], axis=0)
                           ], axis=0) for node in self.nodes]

        self.node_exposures = [nums[0] / nums[1] for nums in urn_counts]
        exposure = mean(self.node_exposures)
        self.exposures.append(exposure)

        return exposure

    def run_step(self):
        picked_balls = [(0 if random() < exposure else 1) for exposure in self.node_exposures]

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
        if self.current >= len(self.nodes):
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
