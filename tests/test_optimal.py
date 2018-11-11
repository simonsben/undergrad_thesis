from network import network
from optimize import optimize_starting, min_steps
from plot import plot_contagion

if __name__ == '__main__':
    net = network(3, op_run=True, fix_start=True)
    net = optimize_starting(net)

    net.run_n_steps(min_steps)
    plot_contagion(net)
