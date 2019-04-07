from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from numpy import linspace, array
from utilities import balls_per_node, save_trials, fig_size, load_csv_col
from execute.run_polya import run_polya
from utilities.plotting import plot_scatter_data

# Define constants
fresh_data = True
num_steps = 250
data_path = '../../data/analysis/uniform_budget.csv'
fig_path = '../../results/analysis/uniform_budget.png'

if fresh_data:
    _, edges = load_airport_and_route(deep_load=True)
    netx = from_edgelist(edges)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)
    bud = N * balls_per_node

    ratios = linspace(.1, .9, 15)
    budgets = [(bud/ratio - bud) for ratio in ratios]
    print(ratios)
    trial_infection = []
    for budget in budgets:
        tmp = round(budget / N)
        B = [tmp] * N
        print(budget, tmp)
        net.set_initial_distribution(black=B)

        infection = run_polya(net, steps=num_steps, trials=5)
        trial_infection.append(infection[len(infection)-1])

    save_trials(trial_infection, data_path, titles=ratios, single_line=True)
else:
    [trial_infection], ratios = load_csv_col(data_path, with_headers=True, parse=float)

ratios = [1/(1+float(ratio)) for ratio in ratios]
data = array([ratios, trial_infection]).astype(float)
plot_scatter_data(data, file_name=fig_path, x_label='$\\frac{R}{R+B}$', y_label='$I_{250}$', size=fig_size,
                  connect=True)
