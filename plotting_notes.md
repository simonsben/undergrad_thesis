# Notes on plotting using NetworkX

## Generating graph

A graph is initialized by calling `G = nx.Graph()`.
Nodes can then be added to the graph by using the `G.add_node(node_id)` call.
The nodes can be connected using `G.add_edge(start_node_id, end_node_id)` (*NOTE:* the edges do not have directions in a graph).

### Batch adding nodes and edges

Nodes and edges can also be added by providing an array of node ids or edges, respectively.
The syntax is as follows:
``` python
nx.add_node_from([id_1, id_2, ...]) # Add nodes from array
nx.add_edge_from([(src_id, dest_id), (src_id, dest_id), ...])   # Add edge from array
```

## Plotting graph

A graph can be plotted (into a *pop-out* window) using the following set of calls

``` python
nx.draw(G)  # NetworkX process graph
plt.draw()  # Matplotlib process graph
plt.show()  # Matplotlib open window
```

## Required libraries

The libraries used are `matplotlib` and `networkX`.
See https://networkx.github.io/documentation/stable/index.html for documentation.