from model import centrality_allocation, network
from execute.import_data import load_airport_and_route
from networkx import from_edgelist
from execute.run_polya import run_polya
from utilities.plotting import plot_over_time

airports, routes = load_airport_and_route(deep_load=True)
netx = from_edgelist(routes)
net = network(len(airports), graph=netx)

centrality_allocation(net)
trial_data = run_polya(net)
print('Optimization complete')

file_name = '../../results/max_entropy/centrality_strategy.png'
plot_over_time(trial_data, title='Centrality allocation strategy', file_name=file_name)
