from execute.import_data import load_airport_and_route

nodes, edges = load_airport_and_route(deep_load=True)

print('Num nodes: ' + str(len(nodes)))
print('Num edges: ' + str(len(edges)))
