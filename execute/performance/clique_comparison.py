from utilities import load_csv_col, fig_size
from utilities.plotting import plot_scatter_data
from numpy import array

# Define constants
base_path = '../../data/clique/'
simple_path = base_path + 'simple.csv'
single_path = base_path + 'simple_single.csv'
popular_path = base_path + 'popular.csv'
fig_path = '../../results/clique/compare.png'
headers = ['Simple Clique', 'Popular Clique']

# Import data
[simple_data], simple_nums = load_csv_col(simple_path, with_headers=True, parse=float)
# [single_data], single_nums = load_csv_col(single_path, with_headers=True, parse=float)
[popular_data], popular_nums = load_csv_col(popular_path, with_headers=True, parse=float)


# Package data
data = array([
    [simple_nums, simple_data],
    # [single_nums, single_data],
    [popular_nums, popular_data]
]).astype(float)[:, :, 1:]

# Plot data
plot_scatter_data(data, multiple=True, leg=headers, x_label='Number of Cliques', y_label='$I_{120}$', connect=True,
                  size=fig_size, file_name=fig_path)
