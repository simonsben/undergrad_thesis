from model.network import network
from matplotlib.pyplot import figure, scatter, xlabel, ylabel, title, savefig, show, plot
from numpy import zeros, nonzero, array


num_trials = 1000
net_degree = 100


def sum_degrees(net, counter):
    for node in net.nodes:
        counter[node.degree] += 1


counter = zeros(net_degree)

for i in range(num_trials):
    net = network(net_degree)
    sum_degrees(net, counter)

for i, count in enumerate(counter):
    counter[i] /= num_trials * net_degree


plot_data = array([(i, counter[i]) for i in range(len(counter)) if counter[i] > 0])

figure()
plot(plot_data[:, 0], plot_data[:, 1], '.')
xlabel('Degree of Node')
ylabel('Fraction of Nodes')
title('Fraction of Nodes with Different Degree')
savefig('../results/degree_frequencies.png')
show()
