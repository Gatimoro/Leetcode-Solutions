class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        dp = [[0]*len(s) for _ in range(len(s))]
        for i, f in enumerate(s):#and
            for j, b in enumerate(rev):
                if f == b:
                    if i != 0 != j: dp[i][j] = dp[i-1][j-1] + 1
                    else: dp[i][j] = 1
                elif j==i==0:
                        continue
                elif (dp[i-1][j] if i!=0 else 0) >= (dp[i][j-1] if j!=0 else 0):
                    dp[i][j] = dp[i-1][j]
                else: dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
"""Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements."""
