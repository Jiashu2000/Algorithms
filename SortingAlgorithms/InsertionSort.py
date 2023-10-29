# Insertion Sort

'''
Insertion sort is a simple sorting algorithm that works similarly to the way
you sort playing cards in your hand. Values from unsorted part are picked and
placed at the correct position in the sorted part.

Insertion sort is fast and best suitable either when the problem size is small
or the data is nearly sorted.

Algorithm:
insertionSort(array)
    mark the first element as sorted
    for each unsorted element x
        extract the element x
        for j <- lastSortedIndex down to 0
            if current element j > x
                move sorted element to the right by 1
        break loop and insert x here
end insertion sort
'''

from typing import List

def insertionSort(array: List[int]) -> List[int]:

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

data = [9, 5, 1, 4, 3]
insertionSort(data)
print("Sorted array in ascending order: ")
print(data)

'''
Time complexity:
    best: o(n), the array is already sorted
    worst: o(n^2), each elemenet has to be compared with other elements, n * (n - 1)
    average: o(n^2)

Space complexity: 
    o(1)

Stability: 
    yes

Applications:
    the array has a small number of elements
    there are only a few elements left to be sorted
'''