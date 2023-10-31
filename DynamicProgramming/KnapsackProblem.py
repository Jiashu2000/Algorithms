# Knapsack Problem

class Knapsack:

    def knapsack01(values, weights, bag):

        # number of items
        n = len(values)
        
        # row i represents item i
        # column j represents weight j
        dp = [[0] * (bag+1) for _ in range(1+n)]

        for i in range(1, n+1):
            for j in range(1, bag + 1):
                if j >= weights[i-1]:
                    # dp[i-1][j]: not choose ith item
                    # dp[i][j-weights[i]] + values[i]: choose the ith item
                    # can repeatedly choose one item
                    #   dp[i][j] = max(dp[i-1][j], dp[i][j - weights[i-1]] + values[i-1])
                    # cannot repeatedly choose one item
                    #   dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1])
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i-1]] + values[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        for i in dp:
            print(i)
        return dp[n][bag]        

if __name__ == "__main__":
    
    val = [60, 100, 120]
    wt = [10, 20, 30]
    w = 50

    Knapsack.knapsack01(val, wt, w)

    val2 = [10, 40, 30, 50]
    wt2 = [5, 4, 6, 3]
    w2 = 10

    Knapsack.knapsack01(val2, wt2, w2)



class Knapsack_eg:

    # naive recursive implementation
    # returns the maximum value that could be put in a knapsack of capacity of W
    def knapsack_naive(self, W, wt, val, n):
        
        # base case:
        if n == 0 or W == 0:
            return 0
        
        # if weight of the nth item is more than the knapsack of capacity W,
        # then this item cannot be included in the optimal solution.
        if (wt[n-1] > W):
            return self.knapsack_naive(W, wt, val, n-1)
        
        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            return max(
                val[n-1] + self.knapsack_naive(W-wt[n-1], wt, val, n-1),
                self.knapsack_naive(W, wt, val, n-1)
            )
    
    '''
    time: o(2^n)
    space: o(n)
    '''

    # memorization implementation
    def knapsack_memo(self, W, wt, val, n, dp):

        # base case
        if n == 0 or W == 0:
            return 0
        
        if dp[n][W] != -1:
            return dp[n][W]
        
        if wt[n-1] <= W:
            dp[n][W] = max(
                val[n-1] + self.knapsack_memo(W - wt[n-1], wt, val, n-1, dp),
                self.knapsack_memo(W, wt, val, n-1, dp)
            )
        else:
            dp[n][W] = self.knapsack_memo(W, wt, val, n-1, dp)
        return dp[n][W]
    '''
    time: o(n * W)
    space: o(n * W) + o(n)
    '''

    # tabulation implementation
    def knapsack_memo(self, W, wt, val, n):
        dp = [[-1] * (W+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for w in range(1, W+1):
                if wt[i-1] < w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])
                else:
                    dp[i][W] = dp[i-1][W]
        
        return dp[n][W]
    '''
    time: o(n * W)
    space: o(n * W)
    '''

    # Space optimized implementation
    def knapsack_optimzed(self, W, wt, val, n):  
        dp = [-1] * (W+1)
        
        for i in range(1, n+1):

            # Starting from back,
            # so that we also have data of previous computation
            # when taking i-1 items
            for w in range(W, 0, -1):
                if wt[i-1] <= w:
                    dp[1][w] = max(dp[w], dp[w-wt[i-1]] + val[i-1])
        
        return dp[W]
    
    '''
    time: o(n * W)
    space: o(W)
    '''