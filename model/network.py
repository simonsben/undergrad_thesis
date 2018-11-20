from typing import List, Any

from utilities.plot import plot_network
from utilities.utilities import balls_per_node, balls_added, generate_plot_network
from model.polya_node import polya_node
from model.polya import run_polya
from copy import deepcopy, copy
from numpy import zeros, mean, sum
from utilities.io import save_network


class network:
    nodes: List[polya_node]

    def __init__(self, n, fix_start=True, pool_size=1):
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
        print('done gen')

    # TODO write call function to clean up deepcopy

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
            node.neighbours = [self.nodes[ind] for ind in neighbour_indexes]

    def calculate_exposure(self):
        delta_balls = self.steps * balls_added
        # ball_counts = zeros((self.n, 2), int)
        # for i, node in enumerate(self.nodes):
        #     tmp_added = delta_balls * node.degree
        #     ball_counts[i] = [node.red, node.init_total + tmp_added]

        ball_counts = [[node.red, (node.init_total + delta_balls) * node.degree] for node in self.nodes]
        urn_counts = [sum([ball_counts[neighbour.id] for neighbour in node], axis=0) for node in self.nodes]

        self.node_exposures = [nums[0] / nums[1] for nums in urn_counts]
        exposure = mean(self.node_exposures)

        return exposure

    def run_step(self):
        run_polya(self.nodes, self.steps, self.pool)
        self.steps += 1
        self.calculate_weights()
        self.calculate_exposure()
        # self.calculate_contagion()

    def run_n_steps(self, n):
        for i in range(n):
            self.run_step()

    def plot_network(self):
        plot_network(self.network_plot, self.weights)

    # Utility function for performing deep opy on object
    def __deepcopy__(self, memodict={}):
        new_net = copy(self)
        new_net.network_plot = deepcopy(self.network_plot)
        new_net.nodes = deepcopy(self.nodes)
        new_net.weights = deepcopy(self.weights)
        new_net.contagion = deepcopy(self.contagion)

        return new_net

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
