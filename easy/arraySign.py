class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val=prod(nums)
        if not val:return 0
        elif val>0:return 1
        return -1
"""sign of product of array"""
