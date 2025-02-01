class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        for i, l1 in enumerate(nums1):
            for j, l2 in enumerate(nums2):
                if l1==l2:
                    dp[i][j]=1+dp[i-1][j-1] if i>0 and j>0 else 1
                else:
                    left,up = dp[i][j-1]if j>0 else 0, dp[i-1][j] if i>0 else 0
                    dp[i][j]=max(left, up)
        return dp[-1][-1]
"""You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way."""
