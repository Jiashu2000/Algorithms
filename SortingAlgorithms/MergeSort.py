# Merge Sort

'''
Merge algorithm is based on divide and conquer technique. It divides the input array into 
two halves. The heart of the merge sort function is the merge() function. Merge sort is the 
only option when you need a stable and o(nlogn) sort.

Merge sort algorithm
mergeSort(A, p, r):
    if p > r:
        return
    q = (p + r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)
'''

def mergeSort(array):
    left = 0
    right = len(array) - 1
    if right <= left:
        return array
    if right - left == 1:
        return [min(array[0], array[1]), max(array[0], array[1])]
    mid = left + (right - left)//2
    a = mergeSort(array[:mid])
    b = mergeSort(array[mid:])
    
    res = [] 
    ptr1, ptr2 = 0, 0
    while ptr1 < len(a) and ptr2 < len(b):
        n1 = a[ptr1]
        n2 = b[ptr2]
        if n1 < n2:
            res.append(n1)
            ptr1 += 1
        else:
            res.append(n2)
            ptr2 += 1
    
    while ptr1 < len(a):
        res.append(a[ptr1])
        ptr1 += 1
    
    while ptr2 < len(b):
        res.append(b[ptr2])
        ptr2 += 1
    
    return res

data = [6, 5, 12, 10, 9, 1]
sorted_data = mergeSort(data)
print('Merge Sort')
print(sorted_data)


'''
Time complexity:
    best: o(nlogn)
    worst: o(nlogn)
    average: o(nlogn)

Space complexity:
    o(n)

Stability:
    Yes

'''