#!/usr/bin/python3
# main.py

import random as rand
from ch04_frequncy_dist_with_histogram import frequencyChart
def list_factory(n, minimum, maximum):
    """
    Makes a list of random integers of size n with integers in [min, max].
    Requires n >= 1 and maximum > minimum.

    :param n: size of the array to be built
    :param min: min value that will appear in the array
    :param max: max value that will appear in the array
    :return:
    """
    if n >= 1:
        if maximum > minimum:
            lst = []
            for i in range(n):
                lst.append(rand.randint(minimum, maximum))
                print(str(lst[i]) + ', ')
            return lst
        else:
            print('maximum must be greater than minimum')
            return [1]
    else:
        print('n must be greater than or equal to 1')
        return [2]

rand.seed("1234")
maximum = 7
minimum = 0
lst1 = list_factory(10, minimum, maximum)
lst2 = list_factory(25, minimum, maximum)
frequencyChart(lst1)
#frequencyChart(lst2)








