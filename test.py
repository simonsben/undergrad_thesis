from network import network
import matplotlib.pyplot as plt
from matplotlib import animation
import networkx as nx

num_nodes = 10
figure = plt.figure('Test figure')


def update_plot(tmp):
    plt.cla()
    net = network(num_nodes)
    graph = net.network_plot
    plot_layout = nx.spring_layout(graph)

    nx.draw_networkx_edges(graph, plot_layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=net.weights, cmap=plt.cm.cool)


test_animation = animation.FuncAnimation(figure, update_plot, interval=500)
plt.show()

