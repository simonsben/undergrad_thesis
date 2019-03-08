from utilities import airpt_cols, rt_cols, re_index, filter_degree, load_csv_col, airport_path, route_path


def load_airport_and_route(filter_data=True):
    # Load airports
    airports = load_csv_col(airport_path, cols=airpt_cols)
    routes = load_csv_col(route_path, cols=rt_cols)
    print('Data loaded')

    if not filter_data:
        return airports, routes

    # Filter data
    airports, routes, route_indexes = filter_degree(airports, routes)
    re_index(airports, route_indexes)

    return airports, route_indexes
