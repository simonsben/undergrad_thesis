from numpy.random import randint as npy_rand
from random import randint as std_rand
from numpy import zeros

num_range = 20
num_runs = 100000

std_count = zeros(num_range, int)
npy_count = zeros(num_range, int)

std_avg = 0
npy_avg = 0

for i in range(num_runs):
    new_std = std_rand(0, num_range-1)
    new_npy = npy_rand(0, num_range)

    std_count[new_std] += 1
    npy_count[new_npy] += 1

    std_avg += new_std
    npy_avg += new_npy

std_avg /= num_runs
npy_avg /= num_runs

print(std_count, npy_count)
print(std_avg, npy_avg)
