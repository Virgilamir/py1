import random

"""merge sort"""


def merge_sort(a):

    if len(a) <= 1:
        return a
    table = len(a) // 2
    left = merge_sort(a[:table])
    right = merge_sort(a[table:])

    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


rand = random.choices(range(1, 1000001), k=10000)


print(merge_sort(rand))
