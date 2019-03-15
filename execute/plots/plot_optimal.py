from model.analytical import optimize_distribution
from utilities import balls_per_node, save_distribution
from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from utilities.plotting import plot_infection
from execute.run_polya import run_polya

airports, routes = load_airport_and_route(deep_load=False)

# TODO make this WAY more efficient... actually gross
netx = from_edgelist(routes)
N = number_of_nodes(netx)
net = network(N, graph=netx)
neighbourhoods = [[neigh.id for neigh in node] for node in net.nodes]
print('Data import and network generated')

# Define constants
budget = balls_per_node * N
R = [balls_per_node] * N
B = [balls_per_node] * N

# Optimize
B, exp = optimize_distribution(neighbourhoods, R, B, budget, debug=True)
save_distribution(B, deep_save=False)

# Test Run
file_name = '../results/optimal/uniform_red.png'
net.set_initial_distribution(R, B)
trial_exposures = run_polya(net)
plot_infection(trial_exposures, file_name=file_name)
