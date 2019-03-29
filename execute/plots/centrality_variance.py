from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from model.optimize import simple_centrality
from utilities import balls_per_node, save_trials, load_csv_col, fig_size
from numpy import var, array, zeros, copy
from utilities.plotting import plot_scatter_data
from execute.run_polya import run_polya
from execute.optimal_distribution import optimal_distribution

# Define constants
fresh_data = False
num_steps = 250
raw_path = '../../data/analysis/variance_runs.csv'
opt_raw_path = '../../data/analysis/opt_variance_runs.csv'
data_path = '../../data/analysis/variance.csv'
fig_path = '../../results/centrality_metrics/variance.png'
labels = ['Centrality', 'Analytical']

if fresh_data:
    nodes, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    x_vals = array(range(1, num_steps+2))
    R = [balls_per_node] * N
    simple_centrality(net, method=2, red=R)

    trial_infections = run_polya(net, steps=num_steps, combine=False)

    B_opt = optimal_distribution(deep_load=True)
    net.set_initial_distribution(R, B_opt)
    opt_infections = run_polya(net, steps=num_steps, combine=False)
else:
    trial_infections = load_csv_col(raw_path, parse=float, trans=True)
    opt_infections = load_csv_col(opt_raw_path, parse=float, trans=True)

trial_var = var(trial_infections, axis=0)
opt_trial_var = var(opt_infections, axis=0)
if fresh_data:
    save_trials(trial_infections, raw_path)
    save_trials(opt_infections, opt_raw_path)
    save_trials([trial_var, opt_trial_var], data_path, titles=labels)


data = zeros((2, len(trial_var)))
opt_data = copy(data)
for i in range(len(trial_var)):
    data[0, i] = opt_data[0, i] = i + 1
    data[1, i] = trial_var[i]
    opt_data[1, i] = opt_trial_var[i]

plot_scatter_data([data, opt_data], file_name=fig_path, x_label='Time steps', y_label='Variance of trials',
                  connect=True, y_format=True, dot_size=20, multiple=True, leg=labels, size=fig_size)
