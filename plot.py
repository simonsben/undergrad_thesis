import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import animation
from utilities import min_steps
from copy import deepcopy
from numpy import mean


# Generate new network
def generate_plot_network(n):
    return nx.barabasi_albert_graph(n, 1)


# Plot network
def plot_network(graph, weights, id=1):
    plot_layout = nx.spring_layout(graph)  # Calculate layout for nodes
    nx.draw_networkx_edges(graph, plot_layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, plot_layout, node_size=100, node_color=weights, cmap=plt.cm.cool)  # Plot nodes

    plt.figure(id)  # Make figure
    plt.draw()  # Matplotlib virtual draw
    plt.axis('off')  # Disable axis
    plt.show()  # Open matplotlib window


def run_update(tmp, network, layout):
    network.run_step()  # Run one polya step
    graph = network.network_plot  # Get pointer to network graph

    plt.cla()  # Clear figure

    plt.title('Network after ' + str(network.steps) + ' steps')  # Add title to figure

    # TODO Display colormap legend
    nx.draw_networkx_edges(graph, layout, alpha=.3)  # Plot edges
    nx.draw_networkx_nodes(graph, layout, node_size=80, node_color=network.weights, cmap=plt.cm.cool)  # Plot nodes


def plot_contagion(network):
    plt.figure('Network contagion over time')
    plt.plot(network.contagion)
    plt.title('Network contagion over ' + str(network.steps) + ' steps')
    plt.show()


def run_and_plot_exposure(network, num_runs=10):
    run_exposures = []
    for i in range(num_runs):
        tmp_net = deepcopy(network)
        tmp_net.run_n_steps(min_steps)

        run_exposures.append(tmp_net.contagion)

    average_exp = mean(run_exposures, 0)
    plt.figure('Exposure over ' + str(min_steps) + 'steps')

    for i in range(num_runs):
        plt.plot(run_exposures[i], label='Run ' + str(i))
    plt.plot(average_exp, label='Average')
    plt.legend(loc='right')
    plt.show()


def animate_network(network):
    figure = plt.figure('Network animation')  # Initialize figure
    layout = nx.spring_layout(network.network_plot)  # Generate layout

    # Run animation
    an = animation.FuncAnimation(figure, run_update, fargs=(network, layout), interval=250, frames=10, repeat=False)

    plt.show()  # Show window
