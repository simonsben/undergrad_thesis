from model.analytical import optimize_distribution
from model.generator import circular_graph, line_graph, wheel_graph
from numpy import array, round


N = 4
balls_per = 5
num_balls = N * balls_per
R = [0] * N
R[0] = num_balls
# R = [balls_per] * N
B = [balls_per] * N
rounds = 3

network = line_graph(N)
print(array(network))

for i in range(rounds):
    optimal = optimize_distribution(network, num_balls, N, R, B)
    B = round(optimal.x)
    print('Optimal ball placement:', R, B)

    optimal = optimize_distribution(network, num_balls, N, B, R)
    R = round(optimal.x)
    print('Optimal ball placement:', R, B)
