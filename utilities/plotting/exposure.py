from matplotlib.pyplot import figure, show, savefig, legend, xlabel, ylabel, rcParams
from utilities import plot_font_size, plot_line_width, fig_size


def plot_infection(trial_exposures, blocking=True, multiple=False, leg=None, title=None, file_name=None, size=None, font_size=None, leg_loc=None):
    size = fig_size if size is None else size
    font_size = plot_font_size if font_size is None else font_size
    steps = len(trial_exposures) if not multiple else len(trial_exposures[0])
    fig = figure(title, figsize=size)
    rcParams.update({'font.size': font_size})
    ax = fig.gca()

    if multiple:
        for data in trial_exposures:
            ax.plot(data, linewidth=plot_line_width)
    else:
        ax.plot(trial_exposures, linewidth=plot_line_width)

    ax.set_ylim(.2, .8)
    ax.set_xlim(0, steps)
    xlabel('Time steps')
    ylabel('Network infection')

    if title is not None: ax.set_title(title)
    if leg is not None and leg_loc is None: legend(leg)
    elif leg_loc is not None: legend(leg, bbox_to_anchor=leg_loc, loc='upper left')

    if file_name is not None:
        try: savefig(file_name, bbox_inches='tight', pad_inches=0)
        except FileExistsError: pass

    if blocking:
        show()
