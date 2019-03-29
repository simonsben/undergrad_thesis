from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes, betweenness_centrality
from model import network
from utilities.plotting import plot_infection, plot_scatter_data
from execute.run_polya import run_polya
from numpy import sum, array, float, linspace
from utilities import balls_per_node, save_trials, load_csv_col, metrics, metric_names

fresh_data = False
time_limit = 250

# Define paths
data_path = '../../data/analysis/solution_convergence.csv'
fig_path = '../../results/analysis/solution_convergence.png'
scat_path = '../../results/analysis/ac_time_N.png'

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
    num_nodes = linspace(1, 100, 20, dtype=int)
    R = [balls_per_node] * N

    # Run trials
    for num in num_nodes:
        total = sum(cents[:num, 1])
        B = [0] * N
        for i in range(num):
            ind = int(round(cents[i, 0]))
            B[ind] = cents[i, 1] / total * budget

        print(sum(B))
        net.set_initial_distribution(black=B, red=R)

        trial_exposures.append(run_polya(net, steps=time_limit))
    trial_exposures = array(trial_exposures)
else:
    trial_exposures, num_nodes = load_csv_col(data_path, with_headers=True, trans=True, parse=float)
    num_nodes = array(num_nodes).astype(float)


# Save and plot data
time_n = len(trial_exposures[0]) - 1
save_trials(trial_exposures, data_path, titles=num_nodes)
# plot_infection(trial_exposures, multiple=True, leg=num_nodes, file_name=fig_path, blocking=False)

time_N_infections = trial_exposures[:, len(trial_exposures) - 1]
data = array([num_nodes, time_N_infections])
plot_scatter_data(data, x_label='Number of Nodes with Black Balls', connect=True,
                  y_label='$I_{' + str(time_n) + '}$', file_name=scat_path, size=(10, 7.5))
