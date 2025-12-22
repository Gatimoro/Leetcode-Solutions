# You are given an array of n strings strs, all of the same length.

# We may choose any deletion indices, and we delete all the characters in those indices for each string.

# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

# Suppose we chose a set of deletion indices answer such that after deletions, the final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible value of answer.length.
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        col_num = len(strs[0])
        dp = [1] * col_num
        for idx in range(col_num - 2, -1, -1):
            for j in range(idx + 1, col_num):
                if all(row[idx] <= row[j] for row in strs):
                    dp[idx] = max(dp[idx], 1 + dp[j])
        return col_num - max(dp)
