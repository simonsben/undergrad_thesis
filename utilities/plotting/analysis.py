from matplotlib.pyplot import figure, show, title, savefig, plot, legend, xlabel, ylabel
from numpy import polyfit, poly1d, linspace, min, max
from utilities.io import save_frequencies
from utilities import fig_size


def plot_w_best_fit(data, _title='Fitted data', filename='', blocking=False, x_label='', y_label='', data_name='', degree=2):
    figure(_title)
    x, y = data[:, 0], data[:, 1]
    plot(x, y, '.k', label='Execution times')

    domain = linspace(min(x), max(x))
    plot(domain, poly1d(polyfit(x, y, degree))(domain), label='Line of best fit')
    legend()

    title(_title)
    xlabel(x_label)
    ylabel(y_label)

    if filename != '':
        savefig(filename)
    if data_name != '':
        save_frequencies(data, data_name)

    show(block=blocking)


def plot_scatter_data(data, multiple=False, file_name=None, leg=None, blocking=True, x_label=None, y_label=None, x_log=False):
    fig = figure(figsize=fig_size)
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

            ax.scatter(run[0, :], run[1, :])
    else:
        ax.scatter(data[0, :], data[1, :])
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
        try: savefig(file_name)
        except FileExistsError: pass

    if blocking: show()
