from model.generator import star_graph, line_graph
from model.extension import ext_sym_k_normal
from model.network import network
from networkx import to_numpy_array, number_of_nodes, from_numpy_array, barabasi_albert_graph
from model.analytical import optimize_distribution
from numpy import round, mean, min, max, array
from utilities.utilities import balls_per_node
from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show, legend, xlim, ylim, savefig

# Define constants
BASE_N = 11
num_trials = 50
num_steps = 200
net_type = 'path'

# Generate graph
# raw_graph = array(star_graph(BASE_N))
raw_graph = array(line_graph(BASE_N))
# raw_graph = to_numpy_array(ext_sym_k_normal(BASE_N))
# raw_graph = to_numpy_array(barabasi_albert_graph(BASE_N, 1))
graph = from_numpy_array(raw_graph)
N = number_of_nodes(graph)

# Make nodes 'connect to self' for functions
for i in range(N):
    raw_graph[i][i] = 1

# Generate network
net = network(number_of_nodes(graph), graph=graph)

# Optimize initial distribution
optimal = round(optimize_distribution(raw_graph, balls_per_node * N, N).x)
uniform = [balls_per_node] * N

# Print distributions
print('Optimal', optimal)
print('Uniform', uniform)

# Define distributions
distributions = [
    [uniform, uniform],
    [optimal, uniform],
    [uniform, optimal],
    [optimal, optimal]
]

# Associate names to distributions
distribution_names = [
    '(R, B)',
    '(R*, B)',
    '(R, B*)',
    '(R*, B*)'
]

# Calculate exposures
exposures = []
for distribution in distributions:
    dist_exposures = []
    net.set_initial_distribution(distribution[0], distribution[1])

    # Run network multiple times then average runs
    for i in range(num_trials):
        net.run_n_steps(num_steps)
        dist_exposures.append(net.exposures)
        net.clear_network()

    exposures.append(mean(dist_exposures, axis=0))

# Plot exposures
figure('Nash equilibrium', figsize=(8, 5))
for i, exposure in enumerate(exposures):
    plot(exposure, label=distribution_names[i])


# Calculate lower and upper y-axis bounds
min_val = max([min(exposures) - .05, 0])
max_val = min([max(exposures) + .05, 1])


# Complete figure
legend()
xlabel('Time')
ylabel('Network exposure')
title('Nash equilibrium for ' + net_type + ' graph')
xlim((0, num_steps))
ylim((min_val, max_val))
savefig('../results/nash/' + net_type + '_' + str(N) + '.png')
show(block=True)
