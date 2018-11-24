from utilities.io import load_frequencies
from glob import glob
from numpy import polyfit, array
from re import compile
from matplotlib.pylab import figure, plot, show, title, legend, gca, savefig, xlabel, ylabel
from matplotlib.ticker import FormatStrFormatter

p = compile('[0-9]+')
list_of_files = glob('..\data\*[0-9].csv')
lines = []

for filename in list_of_files:
    data = load_frequencies(filename)
    network_size = p.findall(filename)[0]

    line = polyfit(data[:, 0], data[:, 1], 2)
    lines.append((network_size, line))


lines = array([[line[0], line[1][0], line[1][1], line[1][2]] for line in lines])
x_vals = lines[:, 0]

figure()
plot(x_vals, lines[:, 1], label='a')
plot(x_vals, lines[:, 2], label='b')
plot(x_vals, lines[:, 3], label='c')

axis = gca()
axis.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))


legend()
title('Constant weights for line of best fit (ax^2 + bx + c)')
xlabel('Number of nodes')
ylabel('Constant value')
show()
