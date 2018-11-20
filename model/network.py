from utilities.plot import generate_plot_network, plot_network
from utilities.utilities import balls_per_node, balls_added
from model.polya_node import polya_node
from random import randint
from model.polya import run_polya
from multiprocessing import Pool
from copy import deepcopy, copy
from numpy import zeros, mean


class network:
    def __init__(self, n, fix_start=False, op_run=False, pool_size=1):
        self.network_plot = generate_plot_network(n)
        self.nodes = []
        self.weights = []
        self.contagion = []
        self.exposure = []
        self.pool = Pool(pool_size)

        self.n = n
        self.steps = 0
        self.current = 0

        self.generate_network(fix_start, op_run)
        self.calculate_weights()
        self.calculate_exposure()

    # TODO write call function to clean up deepcopy

    def calculate_weights(self):
        if len(self.weights) == 0 or len(self.weights) != len(self.nodes):
            self.weights = [0] * len(self.nodes)

        for i in range(len(self.weights)):
            self.weights[i] = self.nodes[i].weight

    def generate_network(self, fix_start, op_run):
        # Generate nodes
        for node in self.network_plot:  # For each node in plot network
            # Randomize initial number of balls
            if not fix_start:
                num_red = randint(1, balls_per_node-1)
                num_black = balls_per_node - num_red
            else:
                num_red = int(balls_per_node / 2)
                if not op_run:
                    num_black = num_red
                else:
                    num_black = 1

            new_node = polya_node(num_red, num_black, node)  # Create new node
            self.nodes.append(new_node)  # Add new node to network

        # Give each node a pointer to its neighbours
        for node in self.network_plot:  # For each node
            for neighbor in self.network_plot.neighbors(node):  # For each neighbour
                self.nodes[node].add_neighbour(self.nodes[neighbor])  # Add neighbour

    def calculate_contagion(self):
        red_total, total_balls = 0, 0     # Initialize counting variables

        for node in self.nodes:                                   # For each node
            total_balls += node.red + node.black                  # Sum total balls
            red_total += node.red                                 # Sum weighted average

        avg_contagion = red_total / total_balls
        self.contagion.append(avg_contagion)    # Add average at time n to list

    def calculate_exposure(self):
        delta_balls = self.steps * balls_added
        counts = zeros(len(self.nodes), dtype=(int, 2))
        exposures = zeros(len(self.nodes))

        for i, node in enumerate(self.nodes):
            tmp_red = node.get_red_count(self.steps)
            tmp_total = node.total_balls + delta_balls
            counts[i] = (tmp_red, tmp_total)

        for i, node in enumerate(self.nodes):
            red_total = counts[i][0]
            total = counts[i][1]
            for neighbour in node:
                red_total += counts[neighbour.id][0]
                total += counts[neighbour.id][1]
            exposures[i] = red_total / total

        self.exposure.append(mean(exposures))

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
