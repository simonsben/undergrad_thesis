from execute.import_data import load_airport_and_route
from networkx import from_edgelist, find_cliques
from model import network, number_of_nodes
from execute.run_polya import run_polya
from utilities.plotting import plot_scatter_data
from numpy import linspace, array
from utilities import balls_per_node, save_trials, fig_size, load_csv_col
from model.optimize import simple_cliques

# Define Constants
fresh_data = True
single_place = True
data_path = '../../data/clique/simple' + ('_single' if single_place else '') + '.csv'
fig_path = '../../results/clique/simple' + ('_single' if single_place else '') + '.png'

if fresh_data:
    # Import data and generate network
    _, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    budget = N * balls_per_node
    net = network(N, graph=netx)
    print('Data import and network generated')

    # Find and sort cliques
    cliques = sorted(find_cliques(netx), key=lambda c: len(c), reverse=True)

    trial_infections = []
    num_cliques = linspace(1, 120, 40).astype(int)
    for num in num_cliques:
        simple_cliques(net, num, budget, cliques=cliques, single_place=single_place)
        trial = run_polya(net, trials=2)
        trial_infections.append(trial[len(trial) - 1])
else:
    trial_infections, num_cliques = load_csv_col(data_path, with_headers=True, parse=float, trans=True)

data = array([num_cliques, trial_infections])
save_trials(trial_infections, data_path, titles=num_cliques, single_line=True)
plot_scatter_data(data, file_name=fig_path, x_label='Number of Cliques', y_label='Time n infection', size=fig_size,
                  connect=True)
