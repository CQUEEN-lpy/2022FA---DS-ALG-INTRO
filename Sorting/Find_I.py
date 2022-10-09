import random
from Sorting.QuickSort import Quick_Sort

def Find_i(a, begin, last):
    if begin >= last:
        if a[begin] == begin:
            return begin
        return -1

    mid = (begin+last) / 2
    mid = int(mid)
    if a[mid] == mid:
        return mid
    elif a[mid] > mid:
        return (Find_i(a, begin, mid-1))
    else:
        return (Find_i(a, mid+1, last))


if __name__ == '__main__':
    num = 20
    l = []
    for i in range(num+1):
        l.append(random.randint(0, 20))
    Quick_Sort(l, 0, num-1)
    print(l)
    print(Find_i(l,0,num-1), l[Find_i(l,0,num-1)])