from utilities.optimization import calculate_coefficients
from matplotlib.pylab import figure, plot, show, title, legend, gca, savefig, xlabel, ylabel, scatter
from matplotlib.ticker import FormatStrFormatter

lines, _ = calculate_coefficients()
x_vals = lines[:, 0]

figure()
scatter(x_vals, lines[:, 1], label='a')
scatter(x_vals, lines[:, 2], label='b')
scatter(x_vals, lines[:, 3], label='c')

axis = gca()
axis.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))


legend()
title('Constant weights for line of best fit (ax^2 + bx + c)')
xlabel('Number of nodes')
ylabel('Constant value')
savefig('../results/line_of_best_fit_coefs.png')
show()
