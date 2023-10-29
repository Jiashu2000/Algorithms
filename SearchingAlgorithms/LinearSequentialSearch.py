# Linear or Sequential Search

def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = [2, 12, 15, 11, 7, 19, 45]
target = 7
print(linearSearch(nums, target))

'''
Time complexity:
    best: o(1)
    average: o(n)
    worst: o(n)
'''