# Library imports
from utilities import generate_network, plot_network
from random import random

# Initialize graph
G, w = generate_network(50)

for i in range(len(w)):
    val = random()
    if val < .1:
        w[i] = .8
    elif val > .9:
        w[i] = .2

plot_network(G, w)
