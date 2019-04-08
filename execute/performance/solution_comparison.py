from utilities import load_csv_col
from utilities.plotting import plot_infection
from matplotlib.pyplot import show
from numpy import float

data_path = '../../data/'
figure_path = '../../results/'
centrality_path = data_path + 'centrality_metrics/'
max_entropy_path = data_path + 'max_entropy/'
opt_path = data_path + 'optimal_distribution/'

versions = ['single_red', 'uniform_red']
optimal_headers = ['Maximum Entropy', 'Centrality', 'Adapted Centrality', 'Clique', 'Numerical Optimal']
centrality_headers = ['Closeness Centrality', 'Eigenvector Centrality', 'Degree Centrality', 'Betweenness Centrality']
max_entropy_headers = ['Eigenvector Centrality', 'Degree Centrality', 'Betweenness Centrality', 'Closeness Centrality']
time_limit = 100

for version in versions:
    # Get data
    centrality_data, _ = load_csv_col(centrality_path + version + '.csv',
                                                       with_headers=True, trans=True, parse=float)
    max_entropy_data, _ = load_csv_col(max_entropy_path + version + '.csv',
                                                         with_headers=True, trans=True, parse=float)
    opt_centrality = load_csv_col(centrality_path + 'opt_' + version + '.csv', trans=True, parse=float)
    opt_analytical = load_csv_col(opt_path + version + '_trial.csv', parse=float)[0]
    opt_clique = load_csv_col(data_path + 'clique/' + version + '.csv', parse=float)[0]

    # Remove data after time-limit for clarity
    centrality_data, _ = centrality_data[:, :time_limit], centrality_headers[0:4]
    max_entropy_data, _ = max_entropy_data[:, :time_limit], max_entropy_headers[0:4]

    # Take optimal metrics
    opt_entropy = max_entropy_data[1]

    # Define paths
    centrality_plot_path = figure_path + 'centrality_metrics/' + version + '.png'
    entropy_plot_path = figure_path + 'max_entropy/' + version + '.png'
    optimal_plot_path = figure_path + 'optimal/' + version + '.png'

    # Plot results
    plot_infection([centrality_data[1], centrality_data[0], centrality_data[3], centrality_data[2]], blocking=False, multiple=True,
                   leg=centrality_headers, file_name=centrality_plot_path)
    plot_infection([max_entropy_data[0], max_entropy_data[3], max_entropy_data[2], max_entropy_data[1]], blocking=False, multiple=True,
                   leg=max_entropy_headers, file_name=entropy_plot_path)
    plot_infection([opt_entropy, centrality_data[2], opt_centrality, opt_clique, opt_analytical],
                   blocking=False, multiple=True, leg=optimal_headers, file_name=optimal_plot_path)

show()  # Keep figures open
