from model.generator import star_graph, line_graph
from model.network import network
from networkx import from_numpy_array
from model.analytical import optimize_distribution
from numpy import array, round, mean, subtract
from utilities.utilities import balls_per_node
from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show, legend, xlim, ylim

# Define constants
N = 10
num_trials = 50
num_steps = 300

# Generate graph
raw_graph = array(star_graph(N))
# raw_graph = array(line_graph(N))
graph = from_numpy_array(raw_graph)

print('Graph', raw_graph)

# Generate network
net = network(N, graph=graph)

# Optimize initial distribution
optimal = round(optimize_distribution(raw_graph, balls_per_node * N, N).x)
uniform = [balls_per_node] * N

print('Optimal', optimal)
print('Uniform', uniform)

distributions = [
    [uniform, uniform],
    [optimal, uniform],
    [uniform, optimal],
    [optimal, optimal]
]

distribution_names = [
    '(R, B)',
    '(R*, B)',
    '(R, B*)',
    '(R*, B*)'
]

exposures = []
for distribution in distributions:
    dist_exposures = []
    net.set_initial_distribution(distribution[0], distribution[1])

    for i in range(num_trials):
        net.run_n_steps(num_steps)
        dist_exposures.append(net.exposures)
        net.clear_network()

    exposures.append(mean(dist_exposures, axis=0))

exposures[2] = subtract(1, exposures[2])

figure('Nash equilibrium')
for i, exposure in enumerate(exposures):
    plot(exposure, label=distribution_names[i])

legend()
xlabel('Time')
ylabel('Network exposure')
title('Nash equilibrium for star graph')
xlim((0, num_steps))
ylim((0, 1))

show(block=True)
