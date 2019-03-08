from matplotlib.pyplot import figure, show, savefig, plot, legend, xlabel, ylabel
from numpy import mean, subtract
from utilities import fig_size

def plot_exposures(default_set, gradient_set, heuristic_set, random_set):
    num_steps = str(len(default_set[0]))
    _title = 'Network exposure over ' + num_steps + ' steps'

    subtract(1, default_set)
    subtract(1, gradient_set)
    subtract(1, heuristic_set)

    figure('Exposure')
    # trial_opacity = .3
    # for exposures in default_set:
    #     plotting(exposures, alpha=trial_opacity)
    #
    # for exposures in gradient_set:
    #     plotting(exposures, alpha=trial_opacity)
    #
    # for exposure in heuristic_set:
    #     plotting(exposure, alpha=trial_opacity)

    plot(mean(subtract(1, default_set), axis=0), label='Uniform average')
    plot(mean(subtract(1, gradient_set), axis=0), label='Gradient average')
    plot(mean(subtract(1, heuristic_set), axis=0), label='Heuristic average')
    plot(mean(subtract(1, random_set), axis=0), label='Random average')

    legend()
    savefig('../results/network_exposure_' + num_steps + '.png')
    xlabel('Time steps')
    ylabel('Network Exposure')
    show()


def plot_over_time(trial_exposures, blocking=True, size=fig_size, multiple=False, leg=None):
    steps = len(trial_exposures) if not multiple else len(trial_exposures[0])
    title = 'Exposure over ' + str(steps) + ' steps'
    fig = figure(title, figsize=size)
    ax = fig.gca()

    if multiple:
        for data in trial_exposures:
            ax.plot(data)
    else:
        ax.plot(trial_exposures)

    ax.set_ylim(0, 1)
    ax.set_xlim(0, steps)
    ax.set_title(title)
    xlabel('Time steps')
    ylabel('Exposure')

    if leg is not None:
        legend(leg)

    if blocking:
        show()
