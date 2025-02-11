class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        if r==0: return [0,0] if nums[0]==target else [-1,-1]
        while l<=r:
            m = (l+r)//2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        if l==len(nums) or nums[l] != target:
            return [-1,-1]
        ans=[l]
        l, r = 0, len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return ans+[r]
"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity"""
