from utilities import load_frequencies
from utilities import plot_w_best_fit

# times = load_frequencies('../data/execution_times.csv')
#
# plot_w_best_fit(times, filename='../results/benchmark.png',
#                 x_label='Network size (# Nodes)', y_label='Optimization time (s)',
#                 _title='Gradient descent execution time')

times = load_frequencies('../data/heuristic_times_500000.csv')

plot_w_best_fit(times, blocking=True, filename='../results/heuristic.png',
                x_label='Network size (# Nodes)', y_label='Optimization time (s)',
                _title='Heuristic method execution time', degree=1)
