# Selection Sort

'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element
from the unsorted part and put it at the begining. The algorithm maintains two subarrays
in a given array: 
    1) the subarray which is already sorted.
    2) remaining subarray which is unsorted.

The selection sort has the property of minimizing the number of swaps. 
It is the best choice when the cost of swapping is high.

Algorithm:
selectionSort(array, size)
    repeat (size - 1) times
    set the first unsorted element as the minimum
    for each of the unsorted elements
        if element < currentMinimum
            set element as new minimum 
    swap minimum with first unsorted position
end selectionSort
'''

def selectionSort(array):
    length = len(array)
    for i in range(length):
        curMin = array[i]
        minIdx = i
        for j in range(i+1, length):
            cur = array[j]
            if cur < curMin:
                curMin = cur
                minIdx = j
        array[i], array[minIdx] = array[minIdx], array[i]


data = [-2, 45, 0, 11, -9]
selectionSort(data)
print("Sorted array in ascending order: ")
print(data)

'''
Time complexity:
    best: o(n^2)
    worst: o(n^2)
    average: o(n^2)

    cycle       no.comparison
      1             (n-1)
      2             (n-2)
      3             (n-3)
      ...           ...
      last          1
    
    Total no.comparisons: (n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2

Space complexity:
    o(1)

Stability:
    No


'''