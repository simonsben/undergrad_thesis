from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from utilities.plotting import plot_scatter_data
from execute.run_polya import run_polya
from numpy import sum, array, float, linspace
from utilities import balls_per_node, save_trials, load_csv_col, metrics

# Choose simulation options
fresh_data = False
time_limit = 250

# Define paths
data_path = '../../data/analysis/solution_convergence.csv'
fig_path = '../../results/analysis/solution_convergence.png'
scat_path = '../../results/analysis/ac_time_N.png'
headers = ['Eigenvalue Centrality', 'Closeness Centrality', 'Degree Centrality', 'Betweenness Centrality']

if fresh_data:
    # Import data and generate network
    _, routes = load_airport_and_route(deep_load=True)
    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    print('Data imported and network generated')

    # Define constants
    budget = balls_per_node * N
    trial_exposures = []
    num_nodes = linspace(1, 100, 20, dtype=int)
    R = [balls_per_node] * N

    # Calculate and sort node centralities
    for ind in metrics:
        centrality_infections = []
        raw_cent = metrics[ind](netx)
        cents = [0] * N
        for key in raw_cent:
            cents[key] = [key, raw_cent.get(key)]
        cents = array(sorted(cents, key=lambda c: c[1], reverse=True))

        # Run trials
        for num in num_nodes:
            total = sum(cents[:num, 1])
            B = [0] * N
            for i in range(num):
                ind = int(round(cents[i, 0]))
                B[ind] = cents[i, 1] / total * budget

            print(sum(B))
            net.set_initial_distribution(black=B, red=R)

            tmp = run_polya(net, steps=time_limit)
            centrality_infections.append(tmp[len(tmp) - 1])
        trial_exposures.append(centrality_infections)

    trial_exposures = array(trial_exposures)
    save_trials(trial_exposures, data_path, titles=num_nodes)
else:
    trial_exposures, num_nodes = load_csv_col(data_path, with_headers=True, trans=True, parse=float)
    num_nodes = array(num_nodes).astype(float)


# plot data
data = []
for trial in trial_exposures:
    data.append([num_nodes, trial])
data = array(data)

plot_scatter_data([data[0], data[1], data[3], data[2]], x_label='Number of Nodes with Black Balls, $m$', connect=True,
                  y_label='$I_{' + str(time_limit) + '}$', file_name=scat_path, size=(10, 7.5), multiple=True,
                  leg=headers, y_bnd=(.21, .420))
