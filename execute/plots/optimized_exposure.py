from execute.import_data import load_airport_and_route
from networkx import from_edgelist
from model import network
from execute.run_polya import run_polya
from utilities.plotting import plot_over_time

airports, routes = load_airport_and_route(deep_load=True)
netx = from_edgelist(routes)
net = network(len(airports), graph=netx)

net.optimize_initial(method=1)
traffic_data = run_polya(net)


title = 'Heuristic performance on filteed data'
# file_name = '../../results/heurist'
plot_over_time(traffic_data, title=title)
