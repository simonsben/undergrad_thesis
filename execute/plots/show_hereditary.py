from execute.import_data import load_airport_and_route
from matplotlib.pyplot import figure, show, legend, savefig
from utilities import dict_to_arr, bin_midpoints, filter_degree, re_index, fig_size
from networkx import degree, from_edgelist
from numpy import histogram

leg = [
    'Unfiltered data',
    'Filtered data'
]

# Raw data
airports, routes = load_airport_and_route(filter_data=False, deep_load=True)
netx = from_edgelist(routes)

degrees = dict_to_arr(degree(netx))
raw_h_data, bins = histogram(degrees, bins=20)
raw_midpoints = bin_midpoints(bins)


# Filtered data
f_airports, _, f_routes = filter_degree(airports, routes)
re_index(f_airports, f_routes)
netx = from_edgelist(f_routes)

degrees = dict_to_arr(degree(netx))
f_h_data, bins = histogram(degrees, bins=20)
f_midpoints = bin_midpoints(bins)


# Plot results
fig = figure('Node degree distribution', figsize=fig_size)
ax = fig.gca()
ax.set_title('Node degree distribution')

ax.scatter(raw_midpoints, raw_h_data)
ax.scatter(f_midpoints, f_h_data)

ax.set_yscale('log')
ax.set_ylabel('Number of nodes')
ax.set_xlabel('Degree')
legend(leg)

savefig('../../results/hereditary.png')

show()
