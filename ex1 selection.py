"""selection sorting"""

import random


def selection_sort(a):

    for i in range(0, len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[m] > a[j]:
                m = j
        if m != i:
            a[m], a[i] = a[i], a[m]
    return a


table = random.choices(range(1, 1000001), k=10000)

print(selection_sort(table))
