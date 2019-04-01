from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from model.optimize import simple_centrality, maximum_entropy
from utilities import balls_per_node, save_trials, load_csv_col, fig_size
from numpy import var, array, zeros, copy
from utilities.plotting import plot_scatter_data
from execute.run_polya import run_polya
from execute.optimal_distribution import optimal_distribution

# Define constants
fresh_data = False
num_steps = 250
num_trials = 15
base_path = '../../data/analysis/'
raw_path = base_path + 'variance_runs.csv'
opt_raw_path = base_path + 'opt_variance_runs.csv'
max_ent_path = base_path + 'max_ent_variance_runs.csv'
fig_path = '../../results/analysis/variance.png'
labels = ['Centrality', 'Maximum Entropy', 'Analytical']

if fresh_data:
    nodes, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    x_vals = array(range(1, num_steps+2))
    R = [balls_per_node] * N

    # Centrality
    simple_centrality(net, method=2, red=R)
    trial_infections = run_polya(net, steps=num_steps, combine=False, trials=num_trials)

    # Analytical
    B_opt = optimal_distribution(deep_load=True)
    net.set_initial_distribution(R, B_opt)
    opt_infections = run_polya(net, steps=num_steps, combine=False, trials=num_trials)

    # Maximum Entropy
    maximum_entropy(net, metric_id=1)
    max_ent_infections = run_polya(net, steps=num_steps, combine=False, trials=num_trials)
else:
    opt_infections = load_csv_col(opt_raw_path, parse=float, trans=True)
    trial_infections = load_csv_col(raw_path, parse=float, trans=True)
    max_ent_infections = load_csv_col(max_ent_path, parse=float, trans=True)

opt_var = var(opt_infections, axis=0)
trial_var = var(trial_infections, axis=0)
max_ent_var = var(max_ent_infections, axis=0)

if fresh_data:
    save_trials(opt_infections, opt_raw_path)
    save_trials(trial_infections, raw_path)
    save_trials(max_ent_infections, max_ent_path)


data = zeros((2, len(trial_var)))
opt_data = copy(data)
max_ent_data = copy(data)
for i in range(len(trial_var)):
    data[0, i] = opt_data[0, i] = max_ent_data[0, i] = i + 1
    data[1, i] = trial_var[i]
    opt_data[1, i] = opt_var[i]
    max_ent_data[1, i] = max_ent_var[i]

plot_scatter_data([data, max_ent_data, opt_data], file_name=fig_path, x_label='Time steps',
                  y_label='Variance of trials', connect=True, y_format=True, dot_size=20, multiple=True,
                  leg=labels, size=fig_size, leg_loc=(.5, .6))
