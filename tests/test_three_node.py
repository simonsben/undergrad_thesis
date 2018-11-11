from network import network
from plot import plot_contagion
from numpy import std
from copy import deepcopy

# TODO run this for lots of iterations to make sure its 'fair'..
# TODO write math things to quantify how many trials are required to be 'fair'
if __name__ == '__main__':
    red_win = 0
    total_runs = 100
    run_contagion = []
    net = network(3, True)

    for i in range(total_runs):
        tmp_net = deepcopy(net)
        tmp_net.run_n_steps(10000)

        contagion = tmp_net.contagion
        is_red_win = contagion[len(contagion)-1] > .5
        if is_red_win:
            red_win += 1

        run_contagion.append(contagion[len(contagion)-1])
        print('run', i, 'done')

    print('Over', total_runs, 'red took', red_win, 'or', red_win / total_runs, 'with', std(run_contagion))


    class tmp:
        def __init__(self, _contagion, steps):
            self.contagion = _contagion
            self.steps = steps


    new_tmp = tmp(run_contagion, 10000)
    plot_contagion(new_tmp)
