from model import network
from model.optimize import maximum_entropy
from execute.import_data import load_airport_and_route
from networkx import from_edgelist
from execute.run_polya import run_polya
from utilities.plotting import plot_infection

airports, routes = load_airport_and_route(deep_load=True)
netx = from_edgelist(routes)
net = network(len(airports), graph=netx)

maximum_entropy(net)
trial_data = run_polya(net)
print('Optimization complete')

file_name = '../../results/centrality_metrics/centrality_strategy.png'
plot_infection(trial_data, title='Centrality allocation strategy', file_name=file_name)
