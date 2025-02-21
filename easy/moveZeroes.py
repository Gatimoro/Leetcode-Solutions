class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            while i < len(nums) and nums[i] == 0:
                i += 1
            if i>=len(nums): nums[j] = 0
            else: nums[j] = nums[i]
            i+=1
"""move all zeros to the right of the array while preserving the original order of the non-zero elements"""
