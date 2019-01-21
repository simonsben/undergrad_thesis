from matplotlib.pyplot import figure, show, title
from mpl_toolkits.mplot3d import Axes3D


# Define exposure function for time 0
def exposure(x, R):
    B = x

    expsr = (R[0] + R[1] + R[2]) / (R[0] + R[1] + R[2] + B[0] + B[1] + B[2])
    if R[0] + R[1] + B[0] + B[1] != 0:
        expsr += (R[0] + R[1]) / (R[0] + R[1] + B[0] + B[1])
    if B[1] + B[2] != 0:
        expsr += (R[1] + R[2]) / (R[1] + R[2] + B[1] + B[2])

    return expsr


# Function to make figure of exposure
def generate_fig(R, num):
    fig = figure('Exposure comparison')
    ax = fig.add_subplot(230 + num, projection='3d')
    num_balls = 15

    x, y, z, c = [], [], [], []

    for i in range(num_balls):
        for j in range(num_balls-i, num_balls):
            k = num_balls - i - j
            exp = exposure((i, j, k), R)
            x.append(i)
            y.append(j)
            z.append(k)
            c.append(exp)

    ax.scatter(x, y, z, c=c, s=50, edgecolor='black', cmap='bwr')
    ax.set_xlabel('Node 1')
    ax.set_ylabel('Node 2')
    ax.set_ylabel('Node 3')
    ax.set_title(str(R))


# Possible red distributions
R_versions = (
    (5, 5, 5),
    (15, 0, 0),
    (0, 15, 0),
    (0, 0, 15),
    (2, 11, 2)
)

# For each version make plot
for num, opt in enumerate(R_versions):
    generate_fig(opt, num+1)

show()
