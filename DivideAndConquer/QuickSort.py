# Quick Sort

def quickSort(nums, left, right):
    if right <= left:
        return
    partitionIdx = partition(nums, left, right)
    print("idx", partitionIdx)
    quickSort(nums, left, partitionIdx - 1)
    quickSort(nums, partitionIdx+1, right)


def partition(nums, left, right):
    pivot = nums[left]
    j = left + 1
    for i in range(left + 1, right + 1):
        cur = nums[i]
        if cur < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    nums[left], nums[j-1] = nums[j-1], nums[left]
    return j-1



array = [-2, 3, -1, 0, 13]
N = len(array)

# Function call
quickSort(array, 0, N - 1)
print(array)

'''
Time Complexity:

Best Case: 
    Ω (N log (N))
    The best-case scenario for quicksort occur when the pivot chosen 
    at the each step divides the array into roughly equal halves.
    In this case, the algorithm will make balanced partitions, leading to efficient Sorting.

Average Case: 
    θ ( N log (N))
    Quicksort’s average-case performance is usually very good in practice, 
    making it one of the fastest sorting Algorithm.

Worst Case: 
    O(N2)
    The worst-case Scenario for Quicksort occur when the pivot at each step 
    consistently results in highly unbalanced partitions. When the array is 
    already sorted and the pivot is always chosen as the smallest or largest element. 
    To mitigate the worst-case Scenario, various techniques are used such as 
    choosing a good pivot (e.g., median of three) and
    using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.

    
Auxiliary Space: 
    O(1)
    if we don’t consider the recursive stack space. 
    If we consider the recursive stack space then, 
    in the worst case quicksort could make O(N).

'''

