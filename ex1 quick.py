"""quick sort"""

import random


def quick_sort(a):
    le = len(a)
    if le <= 1:
        return a
    else:
        piv = a.pop()  # last element

    big_items = []
    small_items = []

    for item in a:
        if item > piv:
            big_items.append(item)
        else:
            small_items.append(item)
    return quick_sort(small_items) + [piv] + quick_sort(big_items)


rand = random.choices(range(1, 1000001), k=10000)
print(quick_sort(rand))
