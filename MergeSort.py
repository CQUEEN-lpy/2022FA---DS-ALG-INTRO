import numpy

def Merge_Sort(a, first, last):
    if first < last:
        mid = int((first + last) / 2)
        Merge_Sort(a, first, mid)
        Merge_Sort(a, mid+1, last)
        Merge(a, first, mid, last)

    o = 0

def Merge(a, first, mid, last):
    i = first
    j = mid+1
    l = []

    for k in range(0, last-first+1):
        if i <= mid and j <= last:
            if a[i] <= a[j]:
                l.append(a[i])
                i += 1
            else:
                l.append(a[j])
                j += 1

        elif i > mid:
            l.append(a[j])
            j += 1
        else:
            l.append(a[i])
            i += 1

    k = 0
    for i in range(first, last+1):
        a[i] = l[k]
        k += 1

if __name__ == '__main__':
    l = numpy.random.randint(100, high=None, size=20, dtype='l').tolist()
    print(l)
    Merge_Sort(l, 0, len(l)-1)
    print(l)
