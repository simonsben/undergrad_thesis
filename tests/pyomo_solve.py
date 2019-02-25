import pyomo.environ as pyomo
from numpy import sum, array

num_balls = 15
N = 3
balls_per_node = int(num_balls / N)
network = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]

B = [5, 5, 5]
R = [5, 5, 5]


def exposure(model):
    expsr = 0
    for node in network:  # For each node
        r_sum, b_sum = 0, 0
        for i, rel in enumerate(node):  # Sum all neighbours
            if rel != 0:  # Only sum if there is a
                r_sum += R[i]
                b_sum += model.Black[i]

        if (r_sum + b_sum) != 0:  # Only add to sum if non-zero denominator.
            expsr += r_sum / (r_sum + b_sum)
        else:
            expsr += .5

    return expsr


def ball_counstraint(model):
    return pyomo.summation(model.Black) == num_balls


uniform = array([num_balls / N] * N)


def optimize_dist(R, B):
    model = pyomo.ConcreteModel()

    model.B = pyomo.RangeSet(0, N)
    model.R = pyomo.RangeSet(0, N)

    # TODO write validation function(s)
    model.Red = pyomo.Param(model.R,
                            within=pyomo.NonNegativeIntegers)

    model.Black = pyomo.Var(model.B,
                            domain=pyomo.NonNegativeIntegers,
                            bounds=(0, num_balls),
                            initialize=lambda x: balls_per_node)

    model.exposure = pyomo.Objective(rule=exposure, sense=pyomo.minimize)
    model.ball_cons = pyomo.Constraint(rule=ball_counstraint)

    solver = pyomo.SolverFactory('ipopt', executable='~/.ipopt/Ipopt-3.12.12/build/bin/ipopt')
    solver.solve(model)

    print(model)


optimize_dist(B, R)
