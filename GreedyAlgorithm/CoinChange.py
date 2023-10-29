# Coin Change

'''
Given a value of V Rs and an infinite supply of each of the denominations 
{1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, 
The task is to find the minimum number of coins and/or notes needed to make the change?
'''


def coinChange(coins, value):
    coins.sort()
    
    p = len(coins) - 1
    res = 0
    
    while value > 0:
        
        while p >= 0 and value >= coins[p]:
            res += value//coins[p]
            value = value%coins[p]
        
        p -= 1
    print(res)
    return res

deno = [1, 2, 5, 10, 20, 50, 
        100, 500, 1000]
coinChange(deno, 93)

     