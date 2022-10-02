import random
import numpy
from Sorting.QuickSort import Quick_Sort

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def Partition(a,first, last):
    pivot = random.randint(first, last)
    p = a[pivot]
    swap(a, pivot, last)
    i = first - 1
    j = first

    while j <= last-1:
        if a[j] < p:
            i += 1
            swap(a, i, j)
        j += 1

    i += 1
    swap(a, i, last)
    return i


def Selection(a, first, last, k):
    result = a[k]
    if first < last:
        sp = Partition(a, first, last)

        if sp == k:
            return a[sp]

        elif sp < k:
            return Selection(a, sp+1, last, k)
        else:
            return Selection(a, first, sp-1, k)
        
    return result


if __name__ == '__main__':
    for _ in range(1, 200):
        l = numpy.random.randint(200, high=None, size=200, dtype='l').tolist()
        selection = random.randint(0, 199)
        pick = Selection(l, 0, len(l) - 1, selection)

        Quick_Sort(l, 0, len(l)-1)
        if pick != l[selection]:
            print('FUCK ME')
        else:
            print('HELL YEAH')






