from model.network import network
from matplotlib.pyplot import figure, scatter, show
from numpy import std
from copy import deepcopy
from utilities.utilities import min_steps

# TODO run this for lots of iterations to make sure its 'fair'..
# TODO write math things to quantify how many trials are required to be 'fair'
if __name__ == '__main__':
    red_win = 0
    total_runs = 100
    run_contagion = []
    net = network(3, True)

    for i in range(total_runs):
        tmp_net = deepcopy(net)
        tmp_net.run_n_steps(min_steps * 2)

        contagion = tmp_net.contagion
        is_red_win = contagion[len(contagion)-1] > .5
        if is_red_win:
            red_win += 1

        run_contagion.append(contagion[len(contagion)-1])
        print('run', i, 'done')

    print('Over', total_runs, 'red took', red_win, 'or', red_win / total_runs, 'with', std(run_contagion))

    figure('Three node trials')
    scatter(list(range(total_runs)), run_contagion)
    show()
