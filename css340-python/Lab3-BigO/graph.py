import matplotlib

matplotlib.use('Agg')

from matplotlib import pyplot as pyp

import numpy as np

import math


def main():

    x, y = np.loadtxt('find2.csv', unpack=True, skiprows=1, delimiter=',')

    pyp.plot(x, y, marker='o', color='green', label='Test Results')

    pyp.plot(x, x/55000, color='red', label='$\\frac{1}{55000}n$')

    pyp.legend(shadow=True, fancybox=True, title='Complexity Formulae')

    pyp.xlabel('List Size (n items)')

    pyp.ylabel('Running Time (ms)')

    pyp.title('BigO complexity of function find2')

    pyp.savefig('find2.png', bbox_inches='tight')


main()

