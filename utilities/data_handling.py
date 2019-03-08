from numpy import array, delete, zeros


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
    edge_indexes = []
    for _, route in enumerate(edges):
        src = node_dict.get(route[0])
        dest = node_dict.get(route[1])
        if src is not None and dest is not None:
            used_nodes.add(int(route[0]))
            used_nodes.add(int(route[1]))

            used_edges.append((src, dest))
            edge_indexes.append(route)

    # Filter un-used airports
    remove = []
    for i, _ in enumerate(filtered_points):
        if not (filtered_points[i, 0] in used_nodes):
            remove.append(i)
    filtered_points = delete(filtered_points, remove, 0)

    return filtered_points, array(used_edges), array(edge_indexes)


def re_index(node_list, edge_list, ind_col=0):
    curr_indexes = {node[ind_col]: i for i, node in enumerate(node_list)}

    for i, node in enumerate(node_list):
        node_list[i, ind_col] = i

    for i, _ in enumerate(edge_list):
        edge_list[i, 0] = curr_indexes.get(edge_list[i, 0])
        edge_list[i, 1] = curr_indexes.get(edge_list[i, 1])


def filter_degree(nodes, edges, d_cut_off=50):
    degrees = {}
    for edge in edges:
        if edge[0] in degrees:
            degrees[edge[0]] += 1
        else:
            degrees[edge[0]] = 1
        if edge[1] in degrees:
            degrees[edge[1]] += 1
        else:
            degrees[edge[1]] = 1

    low_d_nodes = []
    for i, node in enumerate(nodes):
        degree = degrees.get(node[0])
        if degree is None or degree < d_cut_off:
            low_d_nodes.append(i)
    nodes = delete(nodes, low_d_nodes, 0)

    nodes, edge_points, edges = filter_related_data(nodes, edges)

    return nodes, edge_points, edges


def dict_to_arr(d_vals, conv=True):
    d_vals = array(d_vals) if conv else d_vals
    vals = zeros(len(d_vals))

    for val in d_vals:
        if conv:
            vals[val[0]] = val[1]
        else:
            vals[val] = d_vals[val]

    return vals
