from model import network
from utilities import balls_per_node, save_trials, load_csv_col
from networkx import from_edgelist, degree
from numpy import argmax, zeros, array
from execute.run_polya import run_polya
from execute.import_data import load_airport_and_route
from utilities.plotting import plot_infection

# Red distribution (uniform or single)
fresh_data = True
steps = 250
data_name = '../../data/analysis/uniform.csv'
fig_path = '../../results/analysis/uniform.png'

if fresh_data:
    airports, routes = load_airport_and_route(deep_load=True)     # Import data
    N = len(airports)                               # Initialize N
    budget = balls_per_node * N

    netx = from_edgelist(routes)                    # Generate networkx network
    net = network(N, graph=netx)                    # Generate network
    print('Data imported and network generated')

    degrees = array(sorted(degree(netx), key=lambda d: d[0]))[:, 1]
    max_d_node = argmax(degrees)                    # Get index of max degree

    red = zeros(N)
    red[max_d_node] = budget

    # Run basic metrics
    net.set_initial_distribution(red=red)
    exposures = run_polya(net, steps=steps)

    save_trials(exposures, data_name, single_line=True)
else:
    exposures = load_csv_col(data_name, parse=float)


# Plot data
plot_infection(exposures, file_name=fig_path)
