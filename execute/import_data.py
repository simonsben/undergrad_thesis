from utilities import airpt_cols, rt_cols, re_index, filter_degree, load_csv_col, airport_path, route_path


def load_airport_and_route(filter_data=True, deep_load=False):
    # Load airports
    a_path = airport_path if not deep_load else '../' + airport_path
    r_path = route_path if not deep_load else '../' + route_path

    airports = load_csv_col(a_path, cols=airpt_cols)
    routes = load_csv_col(r_path, cols=rt_cols)

    # Filter data
    cutoff = None if filter_data else 0
    airports, routes, route_indexes = filter_degree(airports, routes, d_cut_off=cutoff)
    re_index(airports, route_indexes)

    return airports, route_indexes
