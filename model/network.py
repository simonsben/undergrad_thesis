from typing import List
from utilities import balls_per_node, generate_plot_network, calculate_exposure, save_network
from model.polya_node import polya_node
from numpy import zeros, empty, uint16, array
from random import random
from networkx import spring_layout
from utilities.plotting import plot_optimized_network


class network:
    nodes: List[polya_node]

    def __init__(self, n, graph=None):
        self.network_plot = generate_plot_network(n) if graph is None else graph
        self.graph_layout = None                    # Networkx layout
        self.nodes = empty(n, dtype=polya_node)     # Array of nodes
        self.node_exposures = zeros(n)              # Array of node exposures
        self.ref_distribution = None                # Array of reference exposures
        self.trial_exposure = []                    # List of trial exposures

        self.n = n              # Number of nodes
        self.steps = 0          # Polya step counter
        self.current = 0        # Iteration index

        self.generate_network()     # Generate network
        self.calculate_exposure()   # Calculate network exposure

    # Function to generate network
    def generate_network(self):
        for i, ind in enumerate(self.network_plot):    # Generate nodes
            new_node = polya_node(balls_per_node, balls_per_node, ind)
            self.nodes[ind] = new_node

        for i, node in enumerate(self.nodes):   # Add neighbours to nodes
            neighbour_indexes = [ind for ind in self.network_plot.neighbors(i)]
            self.nodes[i].add_neighbours([self.nodes[ind] for ind in neighbour_indexes])

    # Function to calculate the exposure of the graph
    def calculate_exposure(self):
        return calculate_exposure(self)

    # Function to run one Polya step
    def run_step(self):
        for i, node in enumerate(self.nodes):
            node.add_ball(random() <= self.node_exposures[i])

        self.calculate_exposure()
        self.steps += 1

    # Function to run n Polya steps
    def run_n_steps(self, n):
        if self.steps == 1:     # When possible, pre-allocate array
            trial_exposure = zeros(n)
            trial_exposure[0] = self.trial_exposure[0]
            self.trial_exposure = trial_exposure

        for i in range(n):      # Run steps
            self.run_step()

    # Function to plotting network before and after optimization
    def plot_network(self, index, blocking=True):
        if index == 1:
            self.ref_distribution = self.get_ball_distribution()
        else:
            self.graph_layout = spring_layout(self.network_plot)
            plot_optimized_network(self, blocking)

    # Function to export network topology
    def export_network(self):
        save_network(self.network_plot)

    # Function to set the initial distribution of the network
    def set_initial_distribution(self, red=None, black=None):
        if red is None and black is None: return

        for i, node in enumerate(self.nodes):
            _red = None if red is None else int(round(red[i]))
            _black = None if black is None else int(round(black[i]))

            node.set_initial(_red, _black)
        self.clear_network()

    # Function to bring the network back to time 1
    def clear_network(self):
        for i, node in enumerate(self.nodes):
            self.nodes[i].clear_node()
        self.steps = 0
        self.trial_exposure.clear()
        self.calculate_exposure()

    # Function to load current ball count into node initial counters
    def lock_optimization(self):
        for i, _ in enumerate(self.nodes):
            self.nodes[i].lock_optimization()

    # Function to get ball distributions
    def get_ball_distribution(self, initial=True, black=True):
        balls = zeros(self.n, dtype=uint16)
        for i, node in enumerate(self.nodes):
            if initial:
                balls[i] = node.init_black if black else node.init_red
            else:
                balls[i] = node.black if black else node.red

        return balls

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
