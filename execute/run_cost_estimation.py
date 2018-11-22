from model.network import network
from matplotlib.pylab import scatter, figure, show, savefig
from time import time_ns
from numpy import array
from multiprocessing import Pool


def run_trial(n):
    net = network(n)

    start = time_ns()
    net.optimize_initial(False)
    end = time_ns()

    print('Done', n)
    return n, (end - start) / 1000000000


if __name__ == '__main__':
    num_trials = 10
    max_n = 500
    n = 4
    times = []
    proc_pool = Pool(2)
    n_vals = []

    while n < max_n:
        for i in range(num_trials):
            n_vals.append(n)
        n *= 2

    times = array(proc_pool.map(run_trial, n_vals))

    figure('Time to run')
    scatter(times[:, 0], times[:,  1])
    savefig('../results/optimization_time.png')
    show()
