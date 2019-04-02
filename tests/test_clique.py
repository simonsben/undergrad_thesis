from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from model.optimize import weighted_cliques, calculate_clique_weights
from utilities import balls_per_node, fig_size, save_trials, metrics, metric_names, load_csv_col
from utilities.plotting import plot_scatter_data
from numpy import linspace, array
from execute.run_polya import run_polya

fresh_data = False
fig_path = 'weighted.png'
data_path = 'weighted.csv'

if fresh_data:
    _, edges = load_airport_and_route()
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    print('Data imported')

    budget = balls_per_node * N
    num_cliques = linspace(1, 30, 20).astype(int)
    infections = []

    for metric_id in metrics:
        data = calculate_clique_weights(net, metric_id=metric_id)
        trial_infections = []

        for num in num_cliques:
            weighted_cliques(net, num, budget, data=data)
            trial = run_polya(net, trials=2)
            trial_infections.append(trial[len(trial) - 1])

        infections.append(trial_infections)
else:
    infections, num_cliques = load_csv_col(data_path, with_headers=True, parse=float, trans=True)

num_cliques = list(map(int, num_cliques))
data = array([[num_cliques, infection] for infection in list(infections)]).astype(float)

save_trials(infections, data_path, titles=num_cliques)
plot_scatter_data(data, multiple=True, leg=metric_names, x_label='Number of Cliques', y_label='Time n infection',
                  size=fig_size, connect=True, file_name=fig_path)
