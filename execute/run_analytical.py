from model.analytical import optimize_distribution
from model.generator import circular_graph, line_graph, wheel_graph
from numpy import array, round
from math import floor


N = 7
balls_per = 5
num_balls = N * balls_per
# R = [1] * N
# R[0] = num_balls - (N-1)
R = [0] * N
R[0] = num_balls

B = [balls_per] * N
rounds = 5

network = line_graph(N)
print(array(network))

print(R, B)

for i in range(rounds):
    print('Round', i+1)
    optimal = optimize_distribution(network, num_balls, N, R, B)
    B = round(optimal.x)
    print('Black move:', 'R', R, 'B', B)


    # TODO double check that optimization is flipped
    optimal = optimize_distribution(network, num_balls, N, B, R)
    R = round(optimal.x)
    print('Red move:', 'R', R, 'B', B)
