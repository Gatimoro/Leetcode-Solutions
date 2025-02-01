class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for n,y in pairwise(nums):
            if not (n&1)-(y&1):return False
        return True
"""An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false."""
