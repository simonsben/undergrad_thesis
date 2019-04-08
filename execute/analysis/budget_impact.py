from execute.import_data import load_airport_and_route
from model.optimize import simple_centrality
from networkx import from_edgelist, number_of_nodes, degree
from model import network
from execute.run_polya import run_polya
from utilities import balls_per_node, save_trials, load_csv_col, dict_to_arr
from utilities.plotting import plot_scatter_data
from numpy import argmax, zeros, array, float, linspace

# Choose simulation options
uniform = True
fresh_data = True
time_limit = 250

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/budget_impact/' + file_name + '.png'
scatter_name = '../../results/budget_impact/time_N.png'
data_name = '../../data/budget_impact/' + file_name + '.csv'

if fresh_data:
    # Load data and generate network
    _, routes = load_airport_and_route(deep_load=True)
    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    # Define setup values
    trial_infection = []
    ratios = array(linspace(1, 20, 20))
    budget = balls_per_node * N

    # Define opponent distribution
    if uniform:
        red = [balls_per_node] * N
    else:
        degrees = dict_to_arr(degree(netx))
        red = zeros(N)
        red[argmax(degrees)] = budget

    # Run trial for set of budget ratios
    for ratio in ratios:
        simple_centrality(net, 2, budget_ratio=ratio, red=red, node_restriction=11)

        vals = run_polya(net, steps=time_limit)
        trial_infection.append(vals)
    trial_infection = array(trial_infection)
else:
    trial_infection, ratios = load_csv_col(data_name, with_headers=True, trans=True, parse=float)
    ratios = array(ratios).astype(float)

# Prepare data
time_n = len(trial_infection[0]) - 1
time_N_infections = trial_infection[:, time_n]

# Save and plot data
if fresh_data:
    save_trials(trial_infection, data_name, titles=ratios)

data = array([ratios, time_N_infections])
plot_scatter_data(data, x_label='Black Budget / Red Budget', connect=True,
                  y_label='$I_{' + str(time_n) + '}$', file_name=scatter_name, size=(10, 7.5))
