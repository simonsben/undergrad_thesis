from numpy import array, delete


def within_region(points, region, cols=None, np_arr=True):
    indexes = cols if cols is not None else [1, 2]

    points_in_region = []
    for _, point in enumerate(points):
        x = point[indexes[0]]
        y = point[indexes[1]]

        # NOTE region = [[x_min, x_max], [y_min, y_max]]
        if region[0, 0] <= x <= region[0, 1] and region[1, 0] <= y <= region[1, 1]:
            points_in_region.append(point)

    return array(points_in_region) if np_arr else points_in_region


def filter_related_data(nodes, edges, region=None):
    filtered_points = nodes if region is None else within_region(nodes, region, cols=(2, 1))

    # Filter routes and airports
    node_dict = {val[0]: val[1:] for _, val in enumerate(filtered_points)}
    used_nodes = set()
    used_edges = []
    for _, route in enumerate(edges):
        src = node_dict.get(route[0])
        dest = node_dict.get(route[1])
        if src is not None and dest is not None:
            used_nodes.add(int(route[0]))
            used_nodes.add(int(route[1]))

            used_edges.append((src, dest))

    # Filter un-used airports
    remove = []
    for i, _ in enumerate(filtered_points):
        if not (filtered_points[i, 0] in used_nodes):
            remove.append(i)
    filtered_points = delete(filtered_points, remove, 0)

    return filtered_points, array(used_edges)
