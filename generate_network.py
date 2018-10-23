# Library imports
import networkx as nx
import matplotlib.pyplot as plt

# Initialize graph
n = 50
G = nx.barabasi_albert_graph(n, 1)

# Plot graph
nx.draw(G)
plt.draw()
plt.show()