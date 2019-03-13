from math import fabs
from numpy import zeros


# Function to generate a line network
def path_graph(N):
    return [[(1 if fabs(i - j) <= 1 else 0) for j in range(N)] for i in range(N)]


# Function to generate a circular network
def cycle_graph(N):
    network = path_graph(N)
    network[0][N-1] = 1
    network[N-1][0] = 1

    return network


# Function to generate a star graph
def star_graph(N):
    network = [[(1 if j == i or j == 0 else 0) for j in range(N)] for i in range(N)]
    for i, _ in enumerate(network[0]):
        network[0][i] = 1

    return network


# Function to generate a wheel graph
def wheel_graph(N):
    network = star_graph(N)

    for i, node in enumerate(network):
        left = (i - 1) if (i-1) > 0 else N - 1
        right = (i + 1) if (i+1) < N else 1

        node[left] = 1
        node[right] = 1

    return network


def sym_k_normal(N, k=3):
    network = None
    if k == 2:
        return cycle_graph(N)
    elif k == 3:
        if N % 2 != 0:
            raise ValueError('N must be divisible by 2')

        network = zeros((N, N))
        lim = int(N/2)
        for j in range(2):
            for i in range(lim):
                network[i + j*lim][j*lim + (i-1) % lim] = 1
                network[i + j*lim][j*lim + i] = 1
                network[i + j*lim][j*lim + (i+1) % lim] = 1
        for i in range(lim):
            network[i][i + lim] = 1
            network[i + lim][i] = 1

    return network


# k=2, n=8
# network = [
#     [1, 1, 0, 1, 0, 1, 0, 0],
#     [1, 1, 1, 0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1, 1, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 0],
#     [0, 1, 0, 0, 0, 1, 1, 1],
#     [0, 0, 1, 0, 1, 0, 1, 1]
# ]

# k=3, n=12
# network = [
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
#     [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
# ]