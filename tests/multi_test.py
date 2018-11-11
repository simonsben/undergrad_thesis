from numpy.random import randint
from multiprocessing import Pool


def bla(a):
    return a * a


if __name__ == '__main__':
    input_array = randint(-5, 5, 10)
    proc_pool = Pool(2)

    out = proc_pool.map(bla, input_array)
    print(input_array, out)

