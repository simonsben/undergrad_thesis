from execute.import_data import load_airport_and_route
from matplotlib.pyplot import figure, show, legend, savefig, rcParams
from utilities import dict_to_arr, bin_midpoints, filter_degree, re_index, fig_size
from networkx import degree, from_edgelist
from numpy import histogram, min, max, polyfit, poly1d, linspace, log, delete, exp

leg = [
    'Unfiltered line of best fit',
    'Filtered line of best fit',
    'Unfiltered data',
    'Filtered data',
]
with_best_fit = False

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

to_delete = []
for i, val in enumerate(f_h_data):
    if val == 0:
        to_delete.append(i)
to_delete = sorted(to_delete, reverse=True)
for ind in to_delete:
    f_h_data = delete(f_h_data, ind)
    f_midpoints = delete(f_midpoints, ind)

if with_best_fit:
    fit_degree = 2
    uf_domain = linspace(min(raw_midpoints), max(raw_midpoints))
    f_domain = linspace(min(f_midpoints), max(f_midpoints))

    uf_best_fit = poly1d(polyfit(raw_midpoints, log(raw_h_data), fit_degree))
    f_best_fit = poly1d(polyfit(f_midpoints, log(f_h_data), fit_degree))
else:
    del leg[0]
    del leg[0]

# Plot results
fig = figure(figsize=(9, 6.5))
rcParams.update({'font.size': 18})
ax = fig.gca()

ax.scatter(raw_midpoints, raw_h_data)
ax.scatter(f_midpoints, f_h_data)

if with_best_fit:
    ax.plot(uf_domain, exp(uf_best_fit(uf_domain)))
    ax.plot(f_domain, exp(f_best_fit(f_domain)))

ax.set_yscale('log')
ax.set_ylabel('Number of nodes')
ax.set_xlabel('Degree')
legend(leg)

savefig('../../results/hereditary.png', bbox_inches='tight', pad_inches=0)

show()
