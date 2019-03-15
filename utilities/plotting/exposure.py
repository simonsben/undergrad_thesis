from matplotlib.pyplot import figure, show, savefig, plot, legend, xlabel, ylabel
from utilities import fig_size


def plot_infection(trial_exposures, blocking=True, size=fig_size, multiple=False, leg=None, title=None, file_name=None):
    steps = len(trial_exposures) if not multiple else len(trial_exposures[0])
    # title = 'Exposure over ' + str(steps) + ' steps' if title is None else title
    fig = figure(title, figsize=size)
    ax = fig.gca()

    if multiple:
        for data in trial_exposures:
            ax.plot(data)
    else:
        ax.plot(trial_exposures)

    ax.set_ylim(0, 1)
    ax.set_xlim(0, steps)
    xlabel('Time steps')
    ylabel('Network infection')

    if title is not None:
        ax.set_title(title)

    if leg is not None:
        legend(leg, loc='upper right')

    if file_name is not None:
        try:
            savefig(file_name)
        except:
            pass

    if blocking:
        show()
