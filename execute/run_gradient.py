from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network, optimize_distribution
from utilities import save_distribution, balls_per_node
from time import time

# Import data and generate network
nodes, edges = load_airport_and_route(filter_data=False)
netx = from_edgelist(edges)
N = number_of_nodes(netx)
net = network(N, graph=netx)

# Generate structures for optimization
neighbourhoods = [[neigh.id for neigh in node] for node in net.nodes]
R, B = [balls_per_node] * N, [balls_per_node] * N
budget = balls_per_node * N

# Optimize
start = time()
distribution = optimize_distribution(neighbourhoods, R, B, budget)
end = time()

print('Execution time: ' + str(end-start) + ' s')

save_distribution(distribution)
print(distribution)
