# Binary Search

'''
Binary search is used to find the position of a specific value in a sorted array
by repeatedly dividing the search interval in half

The idea of binary search is to use the information that the array is sorted
and reduce the time complexity to O(logn)

'''


# Iterative Binary Search

def binarySearch_iterative(nums, target):
    left = 0
    right = len(nums) - 1
    # [left, right]
    while left <= right:
        mid = left + (right - left)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

'''
Time complexity:
    o(logn)

Space complexity:
    o(1)

'''

arr = [2, 3, 4, 10, 40]
x = 10
idx = binarySearch_iterative(arr, x)
print(idx)


# Recursive Binary Search

def binarySearch_recursion(nums, target, l, r):
    if r >= l:
        mid = l + (r - l)//2

        if nums[mid] > target:
            return binarySearch_recursion(nums, target, l, mid-1)
        elif nums[mid] < target:
            return binarySearch_recursion(nums, target, mid+1, r)
        else:
            return mid
    return -1

    '''
    Time complexity:
        o(logn)
    
    Space complexity:
        o(1)
        o(logn) if auxiliary space is considered
    '''

arr = [2, 3, 4, 10, 40]
x = 10
idx = binarySearch_recursion(arr, x, 0, len(arr)-1)
print(idx)
