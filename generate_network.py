import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

for i in range(5):
    G.add_node(i)

for i in range(5):
    G.add_edge(i, 1+1)

nx.draw(G)
plt.draw()
plt.show()