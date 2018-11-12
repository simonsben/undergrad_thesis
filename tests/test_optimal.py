from network import network
from optimize import optimize_starting
from plot import run_and_plot_exposure

if __name__ == '__main__':
    net = network(3, op_run=True, fix_start=True)
    net = optimize_starting(net)
    print('Optimal', net)

    run_and_plot_exposure(net)
