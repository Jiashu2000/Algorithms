# Longest Common Subsequence (LCS)

'''
A longest common subsequence (LCS) is defined as the longest subsequence which is common in all given input sequences.

Input: S1 = “AGGTAB”, S2 = “GXTXAYB”
Output: 4
Explanation: The longest subsequence which is present in both strings is “GTAB”.

Input: S1 = “BD”, S2 = “ABCD”
Output: 2
Explanation: The longest subsequence which is present in both strings is “BD”.

'''

class LCS:

    def lcs_naive(self, s1, s2, end1, end2):
        if end1 < 0 or end2 < 0:
            return 0
        if s1[end1] == s2[end2]:
            return 1 + self.lcs_naive(s1, s2, end1-1, end2-1)
        return max(self.lcs_naive(s1, s2, end1-1, end2), self.lcs_naive(s1, s2, end1, end2-1))
    
    '''
    time: o(2*^(m+n))
    space: o(1)
    '''

    # memorization implementation
    def lcs_memo(self, s1, s2, end1, end2, dp):
        if end1 < 0 or end2 < 0:
            return 0
        if dp[end1][end2] != 0:
            return dp[end1][end2]
        if s1[end1] == s2[end2]:
            dp[end1][end2] = 1 + self.lcs_memo(s1, s2, end1-1, end2-1, dp)
        else:
            dp[end1][end2] = max(self.lcs_memo(s1, s2, end1-1, end2, dp), self.lcs_memo(s1, s2, end1, end2-1, dp))
        return dp[end1][end2]
    
    '''
    time: o(m*n)
    space: o(m*n)
    '''

    # tabulation implementation
    def lcs_tabulation(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0] * (len2+1) for _ in range(len1+1)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len1][len2]

    '''
    time: o(m*n)
    space: o(m*n)
    '''

    def lcs_optimzed(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0] * (len2+1) for _ in range(2)]
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s2[j-1]:
                    dp[1][j] = dp[0][j-1] + 1
                else:
                    dp[1][j] = max(dp[0][j], dp[1][j-1])
            dp[0] = dp[1][:]
        return dp[0][len2]

    '''
    time: o(m*n)
    space: o(2n)
    '''