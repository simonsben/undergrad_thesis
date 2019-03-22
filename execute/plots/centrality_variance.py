from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from model.optimize import simple_centrality
from utilities import balls_per_node, save_distribution, save_trials, load_csv_col
from numpy import var, array, zeros
from utilities.plotting import plot_scatter_data
from execute.run_polya import run_polya

# Define constants
fresh_data = False
num_steps = 250
raw_path = '../../data/centrality_metrics/variance_runs.csv'
data_path = '../../data/centrality_metrics/variance.csv'
fig_path = '../../results/centrality_metrics/variance.png'

if fresh_data:
    nodes, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    x_vals = array(range(1, num_steps+2))
    R = [balls_per_node] * N
    simple_centrality(net, method=2, red=R)

    trial_infections = run_polya(net, steps=num_steps, combine=False)
else:
    trial_infections = load_csv_col(raw_path, trans=True, parse=float)

trial_var = var(trial_infections, axis=0)
if fresh_data:
    save_trials(trial_infections, raw_path)
    save_distribution(trial_var, alt_file_name=data_path)


data = zeros((2, len(trial_var)))
for i in range(len(trial_var)):
    data[0, i] = i + 1
    data[1, i] = trial_var[i]

plot_scatter_data(data, file_name=fig_path, x_label='Time steps', y_label='Variance of trials', connect=True,
                  size=(10, 7.5), y_format=True, dot_size=20)
