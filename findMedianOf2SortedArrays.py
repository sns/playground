import math

def getMedian(a, i = 0):
    if i == len(a):
        raise Exception("Invalid index")
    length = len(a) - i
    if length % 2 == 0:
        return (a[i + (length//2) - 1] + a[i + length//2])/2
    return a[i + int(math.floor(length//2))]

def merge(a, b):
    c = []
    k = 0
    i = 0
    j = 0
    while k < len(a) + len(b):
        if i < len(a) and j < len(b):
            if a[i] >= b[j]:
                c.append(b[j])
                j += 1
            else:
                c.append(a[i])
                i += 1
        elif j == len(b):
            c.append(a[i])
            i += 1
        elif i == len(a):
            c.append(b[j])
            j += 1
        k += 1
    return c

def findMedian(a, b):
    if len(a) <= 2 and len(b) <= 2:
        return getMedian(merge(a, b))
    medianA = getMedian(a)
    medianB = getMedian(b)
    
    if medianA == medianB:
        return medianA

    if medianA > medianB:
        indexA = len(a)//2 + 1
        indexB = len(b)//2 - 1 if len(b) % 2 == 0 else len(b)//2  
        return findMedian(a[:indexA], b[indexB:])
    if medianB > medianA:
        indexA = len(a)//2 - 1 if len(a) % 2 == 0 else len(a)//2
        indexB = len(b)//2 + 1
        return findMedian(a[indexA:], b[:indexB])

print(findMedian([1,2,3,4,5,6], [0,0,0,0,10,10]))