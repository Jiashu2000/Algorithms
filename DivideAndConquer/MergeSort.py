# Merge Sort

def mergeSort(nums, left, right):
    if left == right:
        return nums[left:right+1] 
    mid = left + (right - left)//2
    l = mergeSort(nums, left, mid)
    r = mergeSort(nums, mid+1, right)
    res = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(l) and ptr2 < len(r):
        a = l[ptr1]
        b = r[ptr2]
        if a > b:
            res.append(b)
            ptr2 += 1
        else:
            res.append(a)
            ptr1 += 1
    
    while ptr1 < len(l):
        res.append(l[ptr1])
        ptr1 += 1
    
    while ptr2 < len(r):
        res.append(r[ptr2])
        ptr2 += 1
    
    return res

arr = [12, 11, 13, 5, 6, 7]
sorted_arr = mergeSort(arr, 0, len(arr)-1)
print(sorted_arr)

'''
Time Complexity:
    O(N log(N))
 
Auxiliary Space: 
    O(N)

'''