from model import network
from utilities import balls_per_node, dict_to_arr
from networkx import from_edgelist, degree, eigenvector_centrality, closeness_centrality, betweenness_centrality
from numpy import argmax, zeros, sum, copy, array
from execute.run_polya import run_polya
from utilities.plotting import plot_over_time
from execute.import_data import load_airport_and_route


airports, routes = load_airport_and_route()     # Import data
N = len(airports)                               # Initialize N
budget = balls_per_node * N

netx = from_edgelist(routes)                    # Generate networkx network
net = network(N, graph=netx)                    # Generate network
print('Data imported and network generated')

measures = [
    closeness_centrality,
    betweenness_centrality,
    eigenvector_centrality
]
measure_names = [
    'Closeness centrality',
    'Betweenness centrality',
    'Eigenvector centrality'
]

degrees = dict_to_arr(degree(netx))
max_d_node = argmax(degrees)

# red = array([balls_per_node] * N)
red = zeros(N)
red[max_d_node] = budget

exposures = []

for measure in measures:
    centralities = dict_to_arr(measure(netx), conv=False)
    cent_total = sum(centralities)
    print('Measure calculated')

    black = zeros(N)
    for i in range(N):
        black[i] = round(budget * centralities[i] / cent_total)

    net.set_initial_distribution(red, black)
    exposures.append(run_polya(net))

plot_over_time(exposures, leg=measure_names, multiple=True)
