# Quick Sort

'''
Quick sort is a sorting algorithm based on divide and conquer.
An array is divided into subarrays by selecting a pivot element. 
The pivot element should be positioned in such a way that elements less than
pivot are kept on the left side and elements greater than pivot
are on the right side of the pivot.

Algorithm:
quickSort(array, left, right)
    if left < right:
        pivotIdx = partition(array, left, right)
        quickSort(array, left, pivotIdx-1)
        quickSort(array, pivotIdx, right)

partition(array, left, right)
    set right as pivotIdx
    storeIdx <- left - 1
    for i <- left + 1 to right
    if element[i] < pivotElement
        swap element[i] and element[storeIdx]
        storeIdx +=1
    swap pivotElement and element[storeIdx + 1]
    return storeIdx + 1
'''

def quickSort(array, left, right):
    if right <= left:
        return
    pivotIdx = partition(array, left, right)

    quickSort(array, left, pivotIdx -1)
    quickSort(array, pivotIdx+1, right)

def partition(array, left, right):
    pivot = array[left]
    pivotIdx = left
    left += 1
    for i in range(pivotIdx+1, right+1):
        if array[i] < pivot:
            array[left], array[i] = array[i], array[left]
            left += 1
    array[pivotIdx], array[left - 1] = array[left -1], array[pivotIdx]
    return left - 1


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)
quickSort(data, 0, len(data)-1)
print(data)

'''
Time complexity:
    best: o(nlogn), It occurs when the pivot element is always the middle element or near to the middle element.
    worst: o(n^2), It occurs when the pivot element picked is either the greatest or the smallest element.
    average: o(nlogn)

Space complexity:
    o(logn)

Stability:
    No
'''