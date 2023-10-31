# Longest Palindromic Subsequences (LPS)

'''
The Longest Palindromic Subsequence (LPS) is the problem of 
finding a maximum-length subsequence of a given string that is also a Palindrome.

Examples:

Input: S = “GEEKSFORGEEKS”
Output: 5
Explanation: The longest palindromic subsequence we can get is of length 5. 
There are more than 1 palindromic subsequences of length 5, for example: EEKEE, EESEE, EEFEE, …etc.

Input: S = “BBABCBCAB”
Output: 7
Explanation: As “BABCBAB” is the longest palindromic subsequence in it. 
“BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the longest ones.
'''

class LPS:
    
    # naive recursion approach
    def lps_naive(self, s, start, end):
        if start == end:
            return 1
        if end == start + 1:
            if s[end] == s[start]:
                return 2
            return 1

        if s[start] == s[end]:
            return 2 + self.lps_naive(s, start + 1, end - 1)
        return max(self.lps_naive(s, start + 1, end), self.lps_naive(s, start, end - 1))
    
    '''
    time: o(2^n) where n is len(s)
    '''

    # memorization implementation
    def lps_memo(self, s, start, end, dp):

        if start == end:
            return 1
        elif start == end - 1:
            if s[start] == s[end]:
                return 2
            return 1
        
        if dp[start][end] != -1:
            return dp[start][end]

        res = 0
        
        if s[start] == s[end]:
            res = 2 + self.lps_memo(s, start+1, end-1)
        else:
            res = max(self.lps_memo(s, start+1, end), self.lps_memo(s, start, end-1))
        
        dp[start][end] = res
        return res
    '''
    time: o(n^2)
    space: o(n^2)
    '''

    # tabulation implementation
    def lps_tabulation(self, s):
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if j == i+1:
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] == 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
    
    '''
    time: o(n^2)
    space: o(n^2)
    '''

    # space optimized
    def lps_optimized(self, s, start, end):
        n = len(s)
        dp = [[0] * n for _ in range(2)]
        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):
                if j == i:
                    dp[0][j] = 1
                elif j == i+1:
                    if s[i] == s[j]:
                        dp[0][j] = 2
                    else:
                        dp[0][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[0][j] = 2 + dp[1][j-1]
                    else:
                        dp[0][j] = max(dp[1][j], dp[0][j-1])
            '''
            ATTENTION BUG!!!!!! dp[1] = dp[0] 

            Python does not copy by default. names are separate from values, 
            so assigning a name to another name simply makes two names refer to the same object.
            
            list_a = [1,2,3,4] 
            list_b = [5,6,7,8] 
            list_b = list_a 
            Line 3 doesn’t copy the lists - it simply binds the name list_b to the same list object that list_a is bound to.
            '''
            dp[1] = dp[0][:]
        return dp[0][n-1]
    
        
    '''
    time: o(n^2)
    space: o(n)
    '''