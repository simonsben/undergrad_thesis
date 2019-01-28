from math import fabs


# Function to generate a line network
def line_graph(N):
    return [[(1 if fabs(i - j) <= 1 else 0) for j in range(N)] for i in range(N)]


# Function to generate a circular network
def circular_graph(N):
    network = line_graph(N)
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
network = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
]