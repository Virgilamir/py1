"""insertion sorting"""

import random


def insertion_sort(a):

    for i in range(1, len(a)):
        while a[i - 1] > a[i] and i > 0:
            a[i - 1], a[i] = a[i], a[i - 1]
            i = i - 1
    return a


table = random.choices(range(1, 1000001), k=10000)

print(insertion_sort(table))
