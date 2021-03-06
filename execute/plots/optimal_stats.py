from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from utilities import metrics, metric_names, fig_size, balls_per_node
from execute.optimal_distribution import optimal_distribution
from utilities.plotting import plot_scatter_data
from numpy import array
from matplotlib.pyplot import show

_, routes = load_airport_and_route(deep_load=True)
optimal = optimal_distribution(deep_load=True)
netx = from_edgelist(routes)
N = number_of_nodes(netx)
budget = N * balls_per_node

base_path = '../../results/optimal/stats_'


for i, metric_id in enumerate(metrics):
    raw_data = metrics[metric_id](netx)
    m_data = [[key, raw_data.get(key)] for key in raw_data]
    m_data = array(sorted(m_data, key=lambda d: d[0]))
    m_data = m_data[:, 1]

    x, y = [], []
    for j, val in enumerate(m_data):
        # if optimal[j] != 0:
        x.append(m_data[j])
        y.append(optimal[j] / budget)

    data = array([x, y])
    file_name = base_path + metric_names[metric_id].lower().replace(' ', '_') + '.png'
    plot_scatter_data(data, file_name=file_name, blocking=False,
                      x_label='Centrality', y_label='Proportion of Balls allocated', dot_size=30, size=fig_size)
    print('Done ' + metric_names[i])

show()