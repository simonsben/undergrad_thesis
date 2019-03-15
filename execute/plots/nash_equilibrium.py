from model.network import network
from networkx import number_of_nodes, from_edgelist
from execute.optimal_distribution import optimal_distribution
from utilities import balls_per_node
from execute.import_data import load_airport_and_route
from execute.run_polya import run_polya
from utilities.plotting import plot_infection
from utilities import save_trials

# Generate graph
_, routes = load_airport_and_route(deep_load=True)
netx = from_edgelist(routes)
N = number_of_nodes(netx)
net = network(N, graph=netx)

# Optimize initial distribution
optimal = optimal_distribution(deep_load=True)
uniform = [balls_per_node] * N

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
for i, distribution in enumerate(distributions):
    print('Starting' + distribution_names[i])
    net.set_initial_distribution(distribution[0], distribution[1])
    exposures.append(run_polya(net))

# Define constants
fig_path = '../../results/nash/optimal.png'
data_path = '../../data/nash/optimal.png'

# Save and plot data
save_trials(exposures, data_path, titles=distribution_names)
plot_infection(exposures, multiple=True, leg=distribution_names, file_name=fig_path)
