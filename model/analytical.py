from pyomo.environ import minimize, maximize, summation, NonNegativeIntegers, \
    Var, Param, Objective, Constraint, SolverFactory, ConcreteModel, RangeSet, NonNegativeReals
from utilities.utilities import ipopt_path


def optimize_distribution(network, R, B, num_balls, goal='min', print_res=False, debug=False):
    N = len(network)
    goal = minimize if goal == 'min' else maximize

    # Define exposure function
    def exposure(model):
        exp = 0
        for node in network:  # For each node
            r_sum, b_sum = 0, 0
            for ind in node:  # Sum all neighbours
                r_sum += model.Fixed[ind]
                b_sum += model.Variable[ind]

            if (r_sum + b_sum) != 0:  # Only add to sum if non-zero denominator.
                exp += r_sum / (r_sum + b_sum)
            else:
                exp += .5

        return exp / N

    # Constraint function for problem
    def ball_constraint(model):
        return summation(model.Variable) == num_balls

    # Function to initialize black values
    def black_init(_, i):
        return B[i]

    # Function to initialize red values
    def red_init(_, i):
        return R[i]

    # Initialize values
    model = ConcreteModel()
    model.F = RangeSet(0, N - 1)
    model.V = RangeSet(0, N - 1)

    # Initialize fixed balls
    model.Fixed = Param(model.F,
                        within=NonNegativeReals,
                        default=red_init)

    # Initialize variable balls
    model.Variable = Var(model.V,
                         domain=NonNegativeReals,
                         bounds=(0, num_balls),
                         initialize=black_init)

    # Define objective function
    model.exposure = Objective(rule=exposure, sense=goal)

    # Define constraint function
    model.constraint = Constraint(rule=ball_constraint)

    # Initialize (ipopt) solver
    solver = SolverFactory('ipopt', executable=ipopt_path)
    # solver = SolverFactory('bonmin', executable='~/.couenne/Couenne-0.5.7/build/bin/bonmin')
    # solver = SolverFactory('couenne', executable='~/.couenne/Couenne-0.5.7/build/bin/couenne')

    # Solve model
    solver.solve(model, tee=debug)

    # Print resulting distribution
    optimal = [0] * N
    if print_res: print('Variable_Fixed')

    for i in range(N):
        optimal[i] = round(model.Variable[i]())

        if print_res: print(str(i) + ': ' + str(optimal[i]) + '_' + str(round(model.Fixed[i])))
    final_exp = round(model.exposure() * 1000) / 1000
    if print_res: print('Final exposure: ' + str(final_exp))

    return optimal, final_exp
