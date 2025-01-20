class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        guan = (nums[0]*nums[1],nums[-2]*nums[-3])
        return max(guan) * nums[-1] if nums[-1]>0 else min(guan)*nums[-1]
"""Given an integer array nums, find three numbers whose product is maximum and return the maximum product."""
