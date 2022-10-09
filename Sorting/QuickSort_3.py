import random

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def Partition(a, first, last):
    i = first - 1
    j = first - 1
    maxx = max(a[first], a[last])
    minn = min(a[first], a[last])
    for k in range(first, last+1):
        if a[k] >= maxx:
            continue
        elif a[k] <= minn:
            j += 1
            swap(a, k, j)
            i += 1
            swap(a, i, j)
        else:
            j += 1
            swap(a, k, j)
    return i, j, k

def Quick_Sort(a, first, last):
    if (first < last) and (first >= 0):
        i, j, k = Partition(a, first, last)
        if i > first:
            Quick_Sort(a, first, i-1)
        if j > i:
            Quick_Sort(a, i+1, j-1)
        if last > j:
            Quick_Sort(a, j+1, last-1)



if __name__ == '__main__':
    l = [7,3,9,6,1,8,9,9,1,1,2,1]
    Quick_Sort(l, 0, len(l)-1)
    print(l)

