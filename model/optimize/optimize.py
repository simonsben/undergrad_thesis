from model.optimize import gradient_optimize, heuristic_optimize, random_optimize, centrality_allocation


def get_optimization_method(method):
    if method in methods:
        print('Running', method_names.get(method))
        return methods.get(method)

    print('Not found, running', method_names.get(0))
    return gradient_optimize


method_names = {
    0: 'Gradient Descent',
    1: 'Heuristic',
    2: 'Random',
    3: 'Centrality allocation'
}

methods = {
    0: gradient_optimize,
    1: heuristic_optimize,
    2: random_optimize,
    3: centrality_allocation
}
