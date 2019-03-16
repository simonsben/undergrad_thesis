from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes, betweenness_centrality
from model import network
from utilities.plotting import plot_infection, plot_scatter_data
from execute.run_polya import run_polya
from numpy import sum, array, float
from utilities import balls_per_node, save_trials, load_csv_col

# uniform = True
fresh_data = False

# Define paths
data_path = '../../data/centrality_metrics/solution_convergence.csv'
fig_path = '../../results/centrality_metrics/solution_convergence.png'
scat_path = '../../results/centrality_metrics/time_N.png'

if fresh_data:
    # Import data and generate network
    _, routes = load_airport_and_route(deep_load=True)
    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    print('Data imported and network generated')

    # Calculate and sort node centralities
    raw_cent = betweenness_centrality(netx)
    cents = [0] * N
    for key in raw_cent:
        cents[key] = [key, raw_cent.get(key)]
    cents = array(sorted(cents, key=lambda c: c[1], reverse=True))

    # Define constants
    budget = balls_per_node * N
    trial_exposures = []
    num_nodes = [1, 2, 3, 5, 10, 25, 50]

    # Run trials
    for num in num_nodes:
        total = sum(cents[:num, 1])
        B = [0] * N
        for i in range(num):
            B[int(cents[i, 0])] = cents[i, 1] / total * budget

        net.set_initial_distribution(black=B)

        trial_exposures.append(run_polya(net))
else:
    trial_exposures, num_nodes = load_csv_col(data_path, with_headers=True, trans=True, parse=float)
    num_nodes = array(num_nodes).astype(float)


# Save and plot data
save_trials(trial_exposures, data_path, titles=num_nodes)
plot_infection(trial_exposures, multiple=True, leg=num_nodes, file_name=fig_path, blocking=False)

time_N_infections = trial_exposures[:, len(trial_exposures) - 1]
data = array([num_nodes, time_N_infections])
plot_scatter_data(data, x_label='Number of Nodes with Black Balls',
                  y_label='Time-N Infection', x_log=True, file_name=scat_path)
