from utilities.plotting import plot_net_w_routes
from execute.import_data import load_airport_and_route

# Load data
filter_data = True
airports, routes = load_airport_and_route(deep_load=True, filter_data=filter_data)
print('Data filtered')

# Plot airports
file_name = '../../results/airport_locations_filtered.png'
plot_net_w_routes(airports, routes, plot_edges=False, file_name=file_name)
