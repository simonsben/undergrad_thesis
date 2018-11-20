from model.network import network
from time import time_ns
from numpy import mean, std

times = []
for i in range(20):
    net = network(1000)
    print(net.exposures[len(net.exposures)-1])

    start = time_ns()
    net.run_n_steps(100)
    end = time_ns()

    print('execute_time', (end - start) / 1000000000)
    times.append((end - start) / 1000000000)

print(mean(times), std(times))
print(net.exposures[len(net.exposures)-1])

# 2.572643455 0.06732472111681173
