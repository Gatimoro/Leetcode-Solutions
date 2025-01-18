class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max([abs(a-b) for a,b in pairwise(nums+[nums[0]])])
"""Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent."""
