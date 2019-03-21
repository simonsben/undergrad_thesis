from matplotlib.pyplot import figure, show, savefig, legend, rcParams
from numpy import min, max
from utilities import plot_font_size, data_fig_size


def plot_scatter_data(data, multiple=False, file_name=None, leg=None, blocking=True, x_label=None, y_label=None, x_log=False, size=None, font_size=None):
    size = data_fig_size if size is None else size
    font_size = plot_font_size if font_size is None else font_size
    fig = figure(figsize=size)
    rcParams.update({'font.size': font_size, 'mathtext.default':  'regular'})
    ax = fig.gca()

    min_x, max_x, min_y, max_y = 0, 0, 0, 0

    if multiple:
        for run in data:
            tmp_min_x, tmp_max_x = min(run[0, :]), max(run[0, :])
            tmp_min_y, tmp_max_y = min(run[1, :]), max(run[1, :])
            min_x = tmp_min_x if min_x > tmp_min_x else min_x
            max_x = tmp_max_x if max_x < tmp_max_x else max_x
            min_y = tmp_min_y if min_y > tmp_min_x else min_y
            max_y = tmp_max_y if max_y < tmp_max_y else max_y

            ax.scatter(run[0, :], run[1, :], s=80)
    else:
        ax.scatter(data[0, :], data[1, :], s=80)
        min_x, max_x = min(data[0, :]), max(data[0, :])
        min_y, max_y = min(data[1, :]), max(data[1, :])

    ax.set_xlim(min_x, max_x)
    y_delta = (max_y - min_y) * .05
    ax.set_ylim(min_y - y_delta, max_y + y_delta)

    if x_label is not None: ax.set_xlabel(x_label)
    if y_label is not None: ax.set_ylabel(y_label)
    if x_log: ax.set_xscale('log')
    if leg is not None: legend(leg)

    if file_name is not None:
        try: savefig(file_name, bbox_inches='tight', pad_inches=0)
        except FileExistsError: pass

    if blocking: show()
