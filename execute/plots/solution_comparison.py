from utilities import load_csv_col
from utilities.plotting import plot_infection
from matplotlib.pyplot import show
from numpy import float

data_path = '../../data/'
figure_path = '../../results/'
centrality_path = data_path + 'centrality_metrics/'
max_entropy_path = data_path + 'max_entropy/'

versions = ['single_red', 'uniform_red']
optimal_headers = ['Optimal centrality strategy', 'Optimal max entropy strategy', 'Optimal analytical strategy']

for version in versions:
    # Get data
    centrality_data, centrality_headers = load_csv_col(centrality_path + version + '.csv',
                                                       with_headers=True, trans=True, parse=float)
    max_entropy_data, max_entropy_headers = load_csv_col(max_entropy_path + version + '.csv',
                                                         with_headers=True, trans=True, parse=float)
    # Take optimal metrics
    opt_centrality = centrality_data[2]
    opt_entropy = max_entropy_data[1]
    opt_analytical = centrality_data[4]

    # Define paths
    centrality_plot_path = figure_path + 'centrality_metrics/' + version + '.png'
    entropy_plot_path = figure_path + 'max_entropy/' + version + '.png'
    optimal_plot_path = figure_path + 'optimal/' + version + '.png'

    # Plot results
    plot_infection(centrality_data[:4], blocking=False, multiple=True,
                   leg=centrality_headers, file_name=centrality_plot_path)
    plot_infection(max_entropy_data[:4], blocking=False, multiple=True,
                   leg=max_entropy_headers, file_name=entropy_plot_path)
    plot_infection([opt_centrality, opt_entropy, opt_analytical],
                   blocking=False, multiple=True, leg=optimal_headers, file_name=optimal_plot_path)

show()  # Keep figures open
