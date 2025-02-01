class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]
        for i,l1 in enumerate(text1):
            for j,l2 in enumerate(text2):
                if l1==l2:
                    tl=dp[i-1][j-1] if i>0<j else 0
                    dp[i][j] = tl +1
                else:
                    top = dp[i-1][j] if i>0 else 0
                    left = dp[i][j-1] if j>0 else 0
                    dp[i][j] = max(top,left)
        return dp[-1][-1]
"""find longest common subsequence."""
