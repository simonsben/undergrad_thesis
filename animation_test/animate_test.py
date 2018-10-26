import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plot = plt.figure('Test figure')
axis = plot.add_subplot(1, 1, 1)

def update_plot(tmp):
    # random_data = np.random.rand(2, 25)
    x = np.random.rand(1, 25)
    y = np.random.rand(1, 25)
    plt.cla()
    plt.scatter(x, y)

test_animation = animation.FuncAnimation(plot, update_plot, interval=50)
plt.show()
