from numpy import full, argmin, argmax, copy
from three_node.utils import calculate_exposure, get_node
import matplotlib.pyplot as plt


graph = full((5, 2), 5)                                 # Initialize graph
last_graph = copy(graph)
current_exposure = calculate_exposure(graph)            # Initialize starting exposure
print('initial exposure', current_exposure)             # Output starting exposure


exposures = [current_exposure]
while True:                                             # Continue until complete
    min_gradient = get_node(graph, argmax, False)       # Get index of min gradient
    if graph[min_gradient][0] - 1 < 0:                  # If subtraction would set balls to negative
        print('neg val')
        break
    graph[min_gradient][0] -= 1                         # Remove ball from min gradient node

    max_gradient = get_node(graph, argmin, True)        # Get index of max gradient node
    graph[max_gradient][0] += 1                         # Add ball to max gradient node

    tmp_exposure = calculate_exposure(graph)            # Re-calculate exposure

    if current_exposure >= tmp_exposure:                # If last step increased exposure
        graph = last_graph                              # Revert to previous graph
        print('done op')
        break

    current_exposure = tmp_exposure                     # Change was good, make exposure current
    exposures.append(current_exposure)
    last_graph = copy(graph)                            # Take a copy of the graph

print('Final exposure', current_exposure)
print('done', graph)

plt.figure('Exposure over optimization')
plt.plot(exposures)
plt.title('Exposure over optimization')
plt.show()
