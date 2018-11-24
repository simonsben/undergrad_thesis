from typing import List
from utilities.utilities import balls_per_node, balls_added, generate_plot_network, calculate_exposure
from model.polya_node import polya_node
from numpy import zeros, copy
from utilities.io import save_network
from random import random
from utilities.plot import plot_optimized_network
from networkx import spring_layout
from model.optimize import optimize_initial,  heuristic_optimize


class network:
    nodes: List[polya_node]

    def __init__(self, n, fix_start=True, graph=None):
        self.network_plot = generate_plot_network(n) if graph is None else graph
        self.graph_layout = None
        self.nodes = []
        self.weights = []
        self.init_weights = []
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

    def plot_network(self, index, blocking=True):
        if index == 1:
            self.calculate_weights()
            self.init_weights = copy(self.weights)
        else:
            self.calculate_weights()
            self.graph_layout = spring_layout(self.network_plot)
            plot_optimized_network(self, blocking)

    def export_network(self):
        save_network(self.network_plot)

    def optimize_initial(self, lock=True, gradient=True):
        if self.steps > 0:
            raise ValueError('Cannot optimize initial after steps were run')
        if gradient:
            optimize_initial(self)
        else:
            heuristic_optimize(self)

        if lock:
            self.lock_optimization()

    def calculate_weights(self):
        self.weights = zeros(self.n)
        delta_balls = balls_added * self.steps

        for i, node in enumerate(self.nodes):
            self.weights[i] = node.red / (node.init_total + delta_balls)

    def clear_network(self):
        for i, node in enumerate(self.nodes):
            self.nodes[i].clear_node()
        self.steps = 0
        self.exposures = []
        self.calculate_exposure()

    def lock_optimization(self):
        for i, _ in enumerate(self.nodes):
            self.nodes[i].lock_optimization()

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
