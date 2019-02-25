import pyomo.environ as pyomo

vol = 100
abv = 0.040

data = {
    'A': {'abv': 0.045, 'cost': 0.32},
    'B': {'abv': 0.037, 'cost': 0.25},
    'W': {'abv': 0.000, 'cost': 0.05},
}


def beer_blend(vol, abv, data):
    C = data.keys()
    model = pyomo.ConcreteModel()
    model.x = pyomo.Var(C, domain=pyomo.NonNegativeReals)
    model.cost = pyomo.Objective(expr=sum(model.x[c] * data[c]['cost'] for c in C))
    model.vol = pyomo.Constraint(expr=vol == sum(model.x[c] for c in C))
    model.abv = pyomo.Constraint(expr=0 == sum(model.x[c] * (data[c]['abv'] - abv) for c in C))

    solver = pyomo.SolverFactory('glpk', executable='C:\\Users\simon\GPLK\glpsol.exe')
    solver.solve(model)

    print('Optimal Blend')
    for c in data.keys():
        print('  ', c, ':', model.x[c](), 'gallons')
    print()
    print('Volume = ', model.vol(), 'gallons')
    print('Cost = $', model.cost())


beer_blend(vol, abv, data)