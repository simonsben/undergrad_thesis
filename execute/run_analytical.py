from model.analytical import optimize_distribution
from model.generator import cycle_graph, path_graph, wheel_graph
from numpy import array, round, copy
from utilities import balls_per_node, save_distribution
from math import pow

N = 21
balls_per = balls_per_node
num_balls = N * balls_per
R = [balls_per] * N

B = [balls_per] * N
rounds = 2

network = path_graph(N)
print(array(network))

print(R, B)


def r_round(num, places=3):
    val = pow(10, places)
    if type(num) == list:
        for i, tmp in enumerate(num):
            num[i] = round(tmp * val) / val
        return num
    else:
        return round(num * val) / val


for i in range(rounds):
    print('Round', i+1)
    B, exp = optimize_distribution(network, R, B, num_balls)
    print('Black move:', 'R', r_round(R), 'B', r_round(B), exp)

    R, exp = optimize_distribution(network, B, R, num_balls, goal='min')
    print('Red move:', 'R', r_round(R), 'B', r_round(B), exp)

save_distribution(B)
