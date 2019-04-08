from numpy import linspace, array, log
from matplotlib.pyplot import figure, show, rcParams, savefig
from utilities import fig_size

x = linspace(0, 1, 101)
y = array([-a * log(a) + -(1-a) * log(1-a) if a != 0 and a != 1 else 0 for a in x])

fig = figure(figsize=fig_size)
rcParams.update({'font.size': 16, 'mathtext.default': 'regular'})
ax = fig.gca()

ax.plot(x, y, linewidth=3)
ax.set_xlim(0, 1)
ax.set_ylim(0, .8)
ax.set_xlabel('$\\bar{B}_i$')
ax.set_ylabel('$I_0$ = $\\frac{ \\bar{R}_i }{ \\bar{R}_i + \\bar{B}_i }$')

path = '../../results/binary_entropy.png'
savefig(path)
show()
