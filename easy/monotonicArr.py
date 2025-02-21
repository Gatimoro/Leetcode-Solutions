class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        last=nums[0]
        up = True if nums[0]<=nums[-1] else False
        if up:
            for n in range(1,len(nums)):
                if nums[n]<last:return False
                last=nums[n]
        else:
            for n in range(1,len(nums)):
                if nums[n]>last:return False
                last=nums[n]
        return True
"""An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise."""
