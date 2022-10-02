import numpy
import random
def Quick_Sort(a, first, last):
    if first < last:
        sp = Random_Partition(a, first, last)
        Quick_Sort(a, first, sp-1)
        Quick_Sort(a, sp+1, last)

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def Partition(a, first, last):
    p = a[last]
    i = first - 1
    for j in range(first, last):
        if a[j] < p:
            i += 1
            swap(a, i, j)

    i += 1
    swap(a, i, last)
    return i

def Random_Partition(a, first, last):
    pivot = random.randint(first, last)
    swap(a, pivot, last)
    p = a[last]
    i = first - 1
    for j in range(first, last):
        if a[j] < p:
            i += 1
            swap(a, i, j)

    i += 1
    swap(a, i, last)
    return i

if __name__ == '__main__':
    l = numpy.random.randint(20, high=None, size=10, dtype='l').tolist()
    print(l)
    Quick_Sort(l, 0, len(l)-1)
    print(l)

    for i in range(100):
        l = numpy.random.randint(100, high=None, size=20, dtype='l').tolist()
        Quick_Sort(l, 0, len(l) - 1)
        for i in range(1, 20):
            if l[i] < l[i-1]:
                print('Fucking Wrong!')
                exit(0)

