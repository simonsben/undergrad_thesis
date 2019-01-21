from matplotlib.pyplot import figure, show, colormaps, get_cmap
from mpl_toolkits.mplot3d import Axes3D

R = (5, 5, 5)


def exposure(x):
    B = x

    expsr = (R[0] + R[1] + R[2]) / (R[0] + R[1] + R[2] + B[0] + B[1] + B[2])
    if R[0] + R[1] + B[0] + B[1] != 0:
        expsr += (R[0] + R[1]) / (R[0] + R[1] + B[0] + B[1])
    if B[1] + B[2] != 0:
        expsr += (R[1] + R[2]) / (R[1] + R[2] + B[1] + B[2])

    return expsr


fig = figure('Problem surface')
ax = fig.add_subplot(111, projection='3d')
c_map = get_cmap('bwr')

num_balls = 15

points = []

x, y, z, c = [], [], [], []

for i in range(num_balls):
    for j in range(num_balls-i, num_balls):
        k = num_balls - i - j
        exp = exposure((i, j, k))
        x.append(i)
        y.append(j)
        z.append(k)
        c.append(exp)


ax.scatter(x, y, z, c=c, s=50, edgecolor='black', cmap='bwr')
show()
