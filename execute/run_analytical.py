from model.analytical import optimize_distribution
from model.generator import cycle_graph, path_graph, wheel_graph
from numpy import array, round, copy
from utilities import balls_per_node

N = 9
balls_per = balls_per_node
num_balls = N * balls_per
R = [balls_per] * N

B = [balls_per] * N
rounds = 2

network = path_graph(N)
print(array(network))

print(R, B)

for i in range(rounds):
    print('Round', i+1)
    B, exp = optimize_distribution(network, R, B, num_balls)
    print('Black move:', 'R', R, 'B', B, exp)

    # TODO double check that optimization is flipped
    R, exp = optimize_distribution(network, B, R, num_balls, goal='min')
    print('Red move:', 'R', R, 'B', B, exp)
