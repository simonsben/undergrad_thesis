from csv import reader
from numpy import array
from execute.import_data import load_airport_and_route
from networkx import from_edgelist, number_of_nodes
from model import network
from utilities import balls_per_node


def optimal_distribution(deep_load=False):
    path = '../data/optimal_distribution/analytical.csv'
    if deep_load:
        path = '../' + path
    with open(path, 'r') as fl:
        rdr = reader(fl)

        distribution = next(rdr)

    for i, _ in enumerate(distribution):
        distribution[i] = int(distribution[i])

    return array(distribution)


def make_optimal_network(deep_load=False, load_black=True):
    _, routes = load_airport_and_route(deep_load=deep_load)
    netx = from_edgelist(routes)
    N = number_of_nodes(netx)
    net = network(N, graph=netx)

    optimal = optimal_distribution(deep_load=deep_load)
    R = B = [balls_per_node] * N
    if load_black:
        B = optimal
    else:
        R = optimal

    net.set_initial_distribution(R, B)
