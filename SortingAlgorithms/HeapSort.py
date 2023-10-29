# Heap Sort

'''
First convert the array into heap data structure using heapify, 
then one by one delete the root node of the Max-heap and 
replace it with the last node in the heap 
and then heapify the root of the heap. 
Repeat this process until size of heap is greater than 1.

Build a heap from the given input array.
Repeat the following steps until the heap contains only one element:
    Swap the root element of the heap (which is the largest element) with the last element of the heap.
    Remove the last element of the heap (which is now in the correct position).
    Heapify the remaining elements of the heap.
The sorted array is obtained by reversing the order of the elements in the input array.
'''

def heapSort(array):
    n = len(array)
    for i in range(n//2-1, -1, -1):
        heapify(array, n, i)
    
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[largest] < array[l]:
        largest = l
    
    if r < n and array[largest] < array[r]:
        largest = r
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

data = [12, 11, 13, 5, 6, 7]
print(data)
heapSort(data)
print(data)

'''
Time complexity:
    o(nlogn)
    
Space complexity:
    o(logn), due to recursive call stack

'''