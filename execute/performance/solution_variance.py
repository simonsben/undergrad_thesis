from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
# from model.optimize import maximum_entropy
from utilities import balls_per_node, save_trials, load_csv_col, fig_size
from numpy import var, array, zeros
from utilities.plotting import plot_scatter_data
from execute.run_polya import run_polya

# Define constants
fresh_data = True
num_steps = 250
num_trials = 15
max_ent_path = '../../data/analysis/max_ent_variance.csv'
fig_path = '../../results/analysis/variance.png'

if fresh_data:
    nodes, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    x_vals = array(range(1, num_steps+2))
    R = [balls_per_node] * N

    # Maximum Entropy
    # maximum_entropy(net, metric_id=1)
    max_ent_infections = run_polya(net, steps=num_steps, combine=False, trials=num_trials)
else:
    max_ent_infections = load_csv_col(max_ent_path, parse=float, trans=True)

max_ent_var = var(max_ent_infections, axis=0)

if fresh_data:
    save_trials(max_ent_infections, max_ent_path)

max_ent_data = zeros((2, len(max_ent_var)))
for i in range(len(max_ent_var)):
    max_ent_data[0, i] = i + 1
    max_ent_data[1, i] = max_ent_var[i]

plot_scatter_data(max_ent_data, file_name=fig_path, x_label='Time Step, n',
                  y_label='Variance', connect=True, y_format=True, dot_size=10, size=fig_size)
