from scipy.optimize import minimize
from numpy import array, sum, round
# from model.generator import wheel_graph

# x = [R_1, R_2, R_3, B_1, B_2, B_3]
#       0    1    2    3    4    5
N = 12
balls_per = 5
num_balls = N * balls_per
R = [balls_per] * N

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
print(array(network))
for row in network:
    if sum(row) != 4:
        print('Bad row!')
        exit()


# Define exposure function
def exposure(B):
    expsr = 0
    for node in network:                        # For each node
        r_sum, b_sum = 0, 0
        for i, rel in enumerate(node):          # Sum all neighbours
            if rel != 0:            # Only sum if there is a connection
                r_sum += R[i]
                b_sum += B[i]

        if (r_sum + b_sum) != 0:                  # Only add to sum if non-zero denominator.
            expsr += r_sum / (r_sum + b_sum)

    # print(B, expsr)

    return expsr


# Define constraint function
def cons_func(x):
    return sum(x) - num_balls


# Bounds on nodes
b = (0, num_balls)
bounds = [b] * N

# Define constraints and options
cons = {'type': 'eq', 'fun': cons_func}
ops = {'disp': True}

# Define initial conditions
# init = array([balls_per] * N)
init = array([
    # [0, 15, 0, 0, 15, 0]
    # [20, 0, 0, 0, 0, 0, 0, 20]
    [20, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0]
    # [10, 0, 10, 0]
])

# Run optimization
optimal = minimize(exposure, init, constraints=cons, method='SLSQP', options=ops, bounds=bounds)


# print('optimal: ', optimal)
print('Optimal ball placement:', round(optimal.x))
