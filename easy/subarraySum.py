class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        return sum([sum(nums[max(0, i - nums[i]):i+1]) for i in range(len(nums))])
"""You are given an integer array nums of size n. For each index i where 0 <= i < n, define a 
subarray
 nums[start ... i] where start = max(0, i - nums[i]).

Return the total sum of all elements from the subarray defined for each index in the array."""
