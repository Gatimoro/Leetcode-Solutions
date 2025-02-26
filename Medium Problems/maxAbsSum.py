class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sums = list(accumulate([0]+nums))
        return max(sums) - min(sums)
"""Maximum absolute sum of subarray"""
