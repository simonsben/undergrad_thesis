from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from utilities import metrics, metric_names
from execute.optimal_distribution import optimal_distribution
from utilities.plotting import plot_scatter_data
from numpy import array, nonzero, select

_, routes = load_airport_and_route()
optimal = optimal_distribution()
netx = from_edgelist(routes)
N = number_of_nodes(netx)

data = []
for i, metric_id in enumerate(metrics):
    raw_data = metrics[metric_id](netx)
    m_data = [[key, raw_data.get(key)] for key in raw_data]
    m_data = array(sorted(m_data, key=lambda d: d[0]))
    m_data = m_data[:, 1]

    x, y = [], []
    for j, val in enumerate(m_data):
        if optimal[j] != 0:
            x.append(m_data[j])
            y.append(optimal[j])

    data.append((x, y))
    print('Done ' + metric_names[i])

data = array(data)
file_path = '../results/optimal/stats.png'
plot_scatter_data(data, multiple=True, leg=metric_names, file_name=file_path,
                  x_label='Centrality', y_label='Balls allocated')
