class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_o_firsts = accumulate(nums[:-1]) #store the prefix sum up to the first to last number
        full_sum = (sum(nums)+1)//2 #this is to avoid multiplying fir_sum by two each time.
        ans=0
        for fir_sum in sum_o_firsts: 
            if fir_sum >= full_sum:ans+=1 #count how many times the condition we are given is satisfied.
        return ans
"""Desc.
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums."""
