from execute.import_data import load_airport_and_route
from model.optimize import simple_centrality
from networkx import from_edgelist, number_of_nodes, degree
from model import network
from execute.run_polya import run_polya
from utilities import balls_per_node, save_trials, load_csv_col, dict_to_arr
from utilities.plotting import plot_infection
from numpy import argmax, array,  zeros

uniform = False
fresh_data = True

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/budget_impact/' + file_name + '.png'
data_name = '../../data/budget_impact/' + file_name + '.csv'
ratios = [.25, .5, .75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 5, 10, 25, 50]

if fresh_data:
    airports, routes = load_airport_and_route(deep_load=True)

    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    trial_infection = []

    budget = balls_per_node * N
    if uniform:
        red = [budget] * N
    else:
        degrees = dict_to_arr(degree(netx))
        red = zeros(N)
        red[argmax(degrees)] = budget

    for ratio in ratios:
        simple_centrality(net, 2, budget_ratio=ratio, red=red)

        vals = run_polya(net)
        trial_infection.append(vals)
else:
    trial_infection, ratios = load_csv_col(data_name, with_headers=True)

# Save and plot data
if fresh_data:
    save_trials(trial_infection, data_name, titles=ratios)
plot_infection(trial_infection, leg=ratios, multiple=True, file_name=img_name)