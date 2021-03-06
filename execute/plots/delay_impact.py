from execute.import_data import load_airport_and_route
from model.optimize import simple_centrality
from networkx import from_edgelist, number_of_nodes, degree
from model import network
from execute.run_polya import run_polya
from utilities import balls_per_node, save_trials, load_csv_col, dict_to_arr, fig_size
from utilities.plotting import plot_infection, plot_scatter_data
from numpy import argmax, zeros, array, float, linspace

uniform = True
fresh_data = False
time_limit = 250

# Define constants
file_name = 'uniform_red' if uniform else 'single_red'
img_name = '../../results/delay_impact/' + file_name + '.png'
scatter_name = '../../results/delay_impact/time_N.png'
data_name = '../../data/delay_impact/' + file_name + '.csv'

if fresh_data:
    airports, routes = load_airport_and_route(deep_load=True)

    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    trial_infection = []
    # delay = array([0, 1, 2, 3, 5, 10, 25, 50])
    delay = array(linspace(0, 50, 20))

    for time in delay:
        per_node = time + balls_per_node
        budget = N * per_node
        if uniform:
            red = [per_node] * N
        else:
            degrees = dict_to_arr(degree(netx))
            red = zeros(N)
            red[argmax(degrees)] = budget

        print(sum(red), budget, time)
        simple_centrality(net, 2, red=red)

        vals = run_polya(net, steps=time_limit)
        trial_infection.append(vals)
else:
    trial_infection, delay = load_csv_col(data_name, with_headers=True, trans=True, parse=float)
    delay = array(delay).astype(float)

trial_infection = array(trial_infection)
time_n = len(trial_infection[0]) - 1
time_N_infections = trial_infection[:, time_n]

# Save and plot data
if fresh_data:
    save_trials(trial_infection, data_name, titles=delay)

# plot_infection(trial_infection, leg=delay, multiple=True, file_name=img_name, blocking=False)

data = array([delay, time_N_infections])
plot_scatter_data(data, x_label='Time step delay', y_label='$I_{' + str(time_n) + '}$', connect=True,
                  file_name=scatter_name, size=fig_size)
