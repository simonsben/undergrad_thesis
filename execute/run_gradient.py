from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network, optimize_distribution
from utilities import save_distribution, balls_per_node, filter_degree, re_index
from time import time

filter_level = 100

# Import and filter data
nodes, edges = load_airport_and_route(filter_data=False)
nodes, _, edges = filter_degree(nodes, edges, d_cut_off=filter_level)
nodes, edges = re_index(nodes, edges)

# Generate network
netx = from_edgelist(edges)
N = number_of_nodes(netx)
net = network(N, graph=netx)

# Generate structures for optimization
neighbourhoods = [[neigh.id for neigh in node] for node in net.nodes]
R, B = [balls_per_node] * N, [balls_per_node] * N
budget = balls_per_node * N

# Optimize
start = time()
distribution, _ = optimize_distribution(neighbourhoods, R, B, budget)
end = time()

print('Execution time: ' + str(end-start) + ' s')


file_name = '../data/optimal_distribution/f_' + str(filter_level) + '_analytical.csv'
save_distribution(distribution, alt_file_name=file_name)
print(distribution)
