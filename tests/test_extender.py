from networkx import barabasi_albert_graph, info, Graph, degree
from utilities.plot import plot_network
from model.generator import sym_k_normal

NUM_NODES = 20
EDGE_COUNT = 1
EXTENSION_NODES = 8


def make_3_reg(N=EXTENSION_NODES):
    graph = sym_k_normal(N)
    net = Graph()
    net.add_nodes_from([i for i in range(N)])
    for i in range(len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                net.add_edge(i, j)


def add_3_reg(N=EXTENSION_NODES, peak=0, root_node=0):
    graph = sym_k_normal(N)
    net = Graph()

    net.add_nodes_from([i + peak for i in range(peak+1, peak+N)])
    net.add_node(root_node)

    for i in range(len(graph)):
        for j in range(i, len(graph)):
            if graph[i][j] == 1:
                src = i + peak if i != 0 else root_node
                dst = j + peak if j != 0 else root_node
                net.add_edge(src, dst)

    return net


def merge_graphs(A, B):
    B.add_nodes_from(A)
    A.add_edges_from(B.edges())
    return A


network = barabasi_albert_graph(NUM_NODES, EDGE_COUNT)

plot_network(network, save_plot=False, netx_plot=True, blocking=False, _title='Raw Graph')

leaves = []
peak = NUM_NODES

for node in range(NUM_NODES):
    if degree(network, node) == 1:
        leaves.append(node)

        extension = add_3_reg(EXTENSION_NODES, peak, node)
        merge_graphs(network, extension)
        peak += EXTENSION_NODES - 1

plot_network(network, save_plot=False, netx_plot=True, _title='Extended graph')

print('leafs', leaves)
