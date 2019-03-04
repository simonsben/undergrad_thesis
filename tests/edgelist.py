from utilities.plot import plot_network
from networkx import read_weighted_edgelist
from utilities.statistics import degree_distribution
from numpy import mean, median, min, max, std, var, array
from matplotlib.pyplot import show, hist, figure

net = read_weighted_edgelist('../data/us_airports.txt')
print('network generated')

d = degree_distribution(net)
print(mean(d), median(d), min(d), max(d), std(d), var(d))

dist = {}
for i, degree in enumerate(d):
    if degree in dist:
        dist[degree] += 1
    else:
        dist[degree] = 1

dd = []
for _, i in enumerate(dist):
    dd.append((i, dist[i]))

dd = array(dd)


# scatter(dd[:, 0], dd[:, 1])
fig = figure()
ax = fig.gca()
ax.scatter(dd[:, 0], dd[:, 1])
ax.set_yscale('log')

fig = figure()
ax = fig.gca()
ax.hist(d, bins=20)
ax.set_yscale('log')

show()

# plot_network(net, netx_plot=True)
