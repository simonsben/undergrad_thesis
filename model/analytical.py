from scipy.optimize import minimize
from numpy import array, sum, copy


def optimize_distribution(network, num_balls, N, R=None, init=None):
    if R is None:
        R = [num_balls / N] * N

    def exposure(B):
        expsr = 0
        for node in network:  # For each node
            r_sum, b_sum = 0, 0
            for i, rel in enumerate(node):  # Sum all neighbours
                if rel != 0:  # Only sum if there is a connection
                    r_sum += R[i]
                    b_sum += B[i]

            if (r_sum + b_sum) != 0:  # Only add to sum if non-zero denominator.
                expsr += r_sum / (r_sum + b_sum)
            else:
                expsr += .5

        return expsr

    # Define constraint function
    cons_func = lambda x: sum(x) - num_balls

    # Bounds on nodes
    bounds = [(0, num_balls)] * N

    # Define constraints and options
    cons = {'type': 'eq', 'fun': cons_func}
    ops = {'disp': False, 'ftol': 1e-10}

    # Assume uniform if no distribution given
    if init is None:
        init = array([num_balls / N] * N)

    # Run optimization
    optimal = minimize(exposure, init, constraints=cons, method='SLSQP', options=ops, bounds=bounds)
    return optimal


def nash_optimize(network, num_balls, N, _R, _B):
    R = copy(_R)
    B = copy(_B)





