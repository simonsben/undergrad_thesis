from csv import reader
from networkx import from_edgelist
from utilities.statistics import degree_distribution
from matplotlib.pyplot import figure, show

with open('../data/routes.dat') as fl:
    fl_reader = reader(fl)
    data = []

    for i, line in enumerate(fl_reader):
        try:
            source = int(line[3])
            dest = int(line[5])

            data.append((source, dest))
        except ValueError:
            continue

print('Data pulled')

net = from_edgelist(data)
print('Network generated')

dist = degree_distribution(net)

fig = figure()
ax = fig.gca()
ax.hist(dist, bins=20)
ax.set_yscale('log')
show()
