from utilities import load_csv_col
from utilities.plotting import plot_infection
from matplotlib.pyplot import show
from numpy import float

data_path = '../../data/'
figure_path = '../../results/'
centrality_path = data_path + 'centrality_metrics/'
max_entropy_path = data_path + 'max_entropy/'

versions = ['single_red', 'uniform_red']
optimal_headers = ['Maximum Entropy Principle', 'Centrality', 'Gradient Descent']
time_limit = 100

for version in versions:
    # Get data
    centrality_data, centrality_headers = load_csv_col(centrality_path + version + '.csv',
                                                       with_headers=True, trans=True, parse=float)
    max_entropy_data, max_entropy_headers = load_csv_col(max_entropy_path + version + '.csv',
                                                         with_headers=True, trans=True, parse=float)
    opt_centrality = load_csv_col(centrality_path + 'opt_' + version + '.csv', trans=True, parse=float)

    # Remove data after time-limit for clarity
    centrality_data, centrality_headers = centrality_data[:, :time_limit], centrality_headers[0:4]
    max_entropy_data, max_entropy_headers = max_entropy_data[:, :time_limit], max_entropy_headers[0:4]

    # Take optimal metrics
    opt_entropy = max_entropy_data[1]
    opt_analytical = centrality_data[4]

    # Define paths
    centrality_plot_path = figure_path + 'centrality_metrics/' + version + '.png'
    entropy_plot_path = figure_path + 'max_entropy/' + version + '.png'
    optimal_plot_path = figure_path + 'optimal/' + version + '.png'

    # Plot results
    plot_infection(centrality_data[0:4], blocking=False, multiple=True,
                   leg=centrality_headers, file_name=centrality_plot_path)
    plot_infection(max_entropy_data[0:4], blocking=False, multiple=True,
                   leg=max_entropy_headers, file_name=entropy_plot_path)
    plot_infection([opt_entropy, opt_centrality, opt_analytical],
                   blocking=False, multiple=True, leg=optimal_headers, file_name=optimal_plot_path)

show()  # Keep figures open
