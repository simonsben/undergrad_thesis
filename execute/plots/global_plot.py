from matplotlib.pyplot import figure, show
from utilities import load_csv_col, filter_related_data
from numpy import array

airpt_cols = [
    [0, int],       # id
    [6, float],     # lat
    [7, float]      # long
]
rt_cols = [
    [3, int],       # src id
    [5, int]        # dest id
]
region = array([
    [-130, -110],   # x - min, max
    [30, 50]        # y - min, max
])

# Load airports
airports = load_csv_col('../../data/airports.dat', cols=airpt_cols)
routes = load_csv_col('../../data/routes.dat', cols=rt_cols)
print('Data loaded')

# Filter data
airports_red, routes_red = filter_related_data(airports, routes, region)
print('Data filtered')

# Plot airfield locations
fig = figure()
ax = fig.gca()
ax.scatter(airports_red[:, 2], airports_red[:, 1], s=15)            # Plot airports
for _, (src, dest) in enumerate(routes_red):                        # Plot routes
    ax.plot((src[1], dest[1]), (src[0], dest[0]), 'k', alpha=.1)
show()
