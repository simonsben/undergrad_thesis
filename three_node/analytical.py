from scipy.optimize import minimize
from numpy import array

# x = [R_1, R_2, R_3, B_1, B_2, B_3]
#       0    1    2    3    4    5
num_balls = 15
R = [0, 15, 0]
balls_per = num_balls / len(R)


# Define exposure function
def exposure(x):
    B = x[0:3]

    expsr = (R[0] + R[1]) / (R[0] + R[1] + B[0] + B[1]) + \
        (R[0] + R[1] + R[2]) / (R[0] + R[1] + R[2] + B[0] + B[1] + B[2]) + \
        (R[1] + R[2]) / (R[1] + R[2] + B[1] + B[2])

    return expsr


# Define constraint function
def cons_func(x):
    return x[0] + x[1] + x[2] - num_balls


# Bounds on nodes
b = (0, num_balls)
bounds = (b, b, b)

# Define constraints and options
cons = {'type': 'eq', 'fun': cons_func}
ops = {'disp': True}

# Define initial conditions
init = array([balls_per] * 3)

# Run optimization
optimal = minimize(exposure, init, constraints=cons, method='SLSQP', options=ops, bounds=bounds)


print('optimal: ', optimal)
