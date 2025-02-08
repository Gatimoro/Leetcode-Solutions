class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        if zeros>=1: 
            if zeros==1:
                ans=[0]*len(nums)
                z=nums.index(0)
                ans[z]=prod(nums[:z])*prod(nums[z+1:])
                return ans
            return [0]*len(nums)
        pro = prod(nums)
        ans = [pro] * len(nums)
        for num in range(len(nums)):
            ans[num]//=nums[num]
        return ans
"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 """
