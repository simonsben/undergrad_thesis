from networkx import Graph, degree, number_of_nodes
from model.generator import sym_k_normal
from utilities.utilities import extension_nodes


# TODO re-write to make faster
# Function to generate a regular graph extension
def gen_reg(peak=0, root_node=0, N=extension_nodes, reg_num=3):
    graph = sym_k_normal(N, reg_num)    # Generate adjacency matrix
    net = Graph()   # Initialize new graph

    # Add nodes to graph
    net.add_nodes_from([i for i in range(peak+1, peak+N)])
    net.add_node(root_node)

    # Add edges to graph
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] == 1:
                src = i + peak if i != 0 else root_node
                dst = j + peak if j != 0 else root_node
                net.add_edge(src, dst)

    return net


# Merge graphs (used to add extension to base graph)
def merge_graphs(base, ext):
    base.add_nodes_from(ext)
    base.add_edges_from(ext.edges())


# Generate extension and merge in for leaf nodes
def extend_network(base):
    peak = N = number_of_nodes(base)

    for node in range(N):
        if degree(base, node) == 1:
            extension = gen_reg(peak, node)
            merge_graphs(base, extension)
            peak += extension_nodes - 1
