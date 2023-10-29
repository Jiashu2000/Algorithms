# Bubble Sort

'''
Bubble sort is the sorting algorithm that works by repeatedly swapping the adjacent
elements if they are in the wrong order. After each iteration or pass, the largest
element reaches the end (in case of ascending order) or the smallest element
reaches the end (in case of descending order). The pass through the list is repeated 
until the list is sorted. This algorithm is not suitable for large data sets as its
average and worst case complexity are of o(n^2) where n is the number of items.

Algorithm:
bubbleSort(array)
    for i <- 1 to indexOfLastUnsortedElement - 1:
        if leftElement > rightElement:
            swap leftElement and rightElement
end bubbleSort
'''

def bubbleSort(array):
    for j in range(len(array)):
        for i in range(1, len(array) - j):
            if array[i] < array[i-1]:
                array[i-1], array[i] = array[i], array[i-1]

data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print("Sorted array in ascending order")
print(data)


'''
Optimized bubble sort:
if the swapped is False from the last iteration, it means that
rest of the array is already sorted.
'''
def optimized_bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(1, len(array) - i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                swapped = True
        if not swapped:
            break

data = [-2, 45, 0, 11, -9]
optimized_bubbleSort(data)
print("Sorted array in ascending order")
print(data)


'''
Time complexity:
    best: o(n)
    worst: o(n^2)
    average: o(n^2)

Space complexity:
    o(1)

Stability:
    Yes
'''