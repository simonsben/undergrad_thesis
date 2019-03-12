from re import compile
from glob import glob
from utilities import load_frequencies, save_frequencies
from numpy import polyfit, array


def calculate_coefficients(save=True):
    p = compile('[0-9]+')
    list_of_files = glob('..\data\*[0-9].csv')
    lines = []

    for filename in list_of_files:
        data = (load_frequencies(filename))
        network_size = p.findall(filename)[0]

        line = polyfit(data[:, 0], data[:, 1], 2)
        lines.append((network_size, line))

    lines = array([[line[0], line[1][0], line[1][1], line[1][2]] for line in lines]).astype(float)
    sorted(lines, key=lambda l: l[0])

    a = polyfit(lines[:, 0], lines[:, 1], 1)
    b = polyfit(lines[:, 0], lines[:, 2], 1)
    c = polyfit(lines[:, 0], lines[:, 3], 1)
    generator = array([a, b, c])

    if save:
        save_frequencies(lines, '../data/ball_gen_data.csv')
        save_frequencies(generator, '../data/ball_generator.csv')

    return lines, generator

