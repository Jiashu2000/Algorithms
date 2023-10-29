# Job Sequencing Problem

'''
Given an array of jobs where every job has a deadline and associated profit if the job is finished before the deadline. 
It is also given that every job takes a single unit of time, so the minimum possible deadline for any job is 1. 
Maximize the total profit if only one job can be scheduled at a time.


Follow the given steps to solve the problem:

Sort all jobs in decreasing order of profit. 
Iterate on jobs in decreasing order of profit.For each job , do the following : 
Find a time slot i, such that slot is empty and i < deadline and i is greatest.Put the job in 
this slot and mark this slot filled. 
If no such i exists, then ignore the job. 
'''

def jobSequence(arr, t):

    # sort the job list based on profit in a descending order
    # o(n * logn)
    arr.sort(key = lambda l: l[2])
    
    # record if a time slot is used or not
    used = [False] * (t+1)
    # store final result
    res = [None] * (t+1)
    # ptr for the job list. start from the end, the most profit job
    i = len(arr) - 1
    
    while i >= 0 and t > 0:
        # the most profit job and its deadline
        cur = arr[i]
        d = cur[1]
        # find the last avaiable timeslot for the job
        # o(n)
        for j in range(d, 0, -1):
            if not used[j]:
                res[j] = cur
                used[j] = True
                t -= 1
                break
        i -= 1

    
    print(res[1: ])
    return res[1:]

if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
              ['b', 1, 19],
              ['c', 2, 27],
              ['d', 1, 25],
              ['e', 3, 15]]
    jobSequence(arr, 3)    

'''
time complexity:
    o(n^2)

space complexity:
    o(n)
'''

import heapq

# using priority queue
def jobSequence_pq(arr, t):
    
    # sort the job list based on deadline in a descending order
    arr.sort(key = lambda l: -l[1])
    # store result
    res = [None] * (t + 1)
    
    # ptr for the job list
    i = 0
    # current time and priority queue to store jobs that have a deadline later than
    # th current time.
    curtime = t
    curlist = []

    while curtime >= 0:

        while i < len(arr) and arr[i][1] >= curtime:
            heapq.heappush(curlist, (-arr[i][2], arr[i][1], arr[i][0]))
            i += 1
        
        top = heapq.heappop(curlist)
        job = [top[2], top[1], -top[0]]
        res[curtime] = job
        curtime -= 1

    print(res[1:])
    return res[1:]

if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
              ['b', 1, 19],
              ['c', 2, 27],
              ['d', 1, 25],
              ['e', 3, 15]]
    jobSequence_pq(arr, 3)  

'''
time complexity:
    o(n * logn)

space complexity:
    o(n)

'''
            