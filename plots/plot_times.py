from utilities.io import load_frequencies
from utilities.plot import plot_w_best_fit

times = load_frequencies('../data/execution_times.csv')

plot_w_best_fit(times, blocking=True, filename='../results/benchmark.png',
                x_label='Network size (# Nodes)', y_label='Optimization time (s)',
                _title='Gradient descent execution time')
