from execute.import_data import load_airport_and_route
from utilities import filter_degree, re_index
from networkx import diameter, from_edgelist

nodes, edges = load_airport_and_route(deep_load=True, filter_data=False)

print('Raw data')
print('Num nodes: ' + str(len(nodes)))
print('Num edges: ' + str(len(edges)))

nodes, _, edges = filter_degree(nodes, edges)
nodes, edges = re_index(nodes, edges)
netx = from_edgelist(edges)

print('Filtered data')
print('Num nodes: ' + str(len(nodes)))
print('Num edges: ' + str(len(edges)))
print('Diameter: ' + str(diameter(netx)))
