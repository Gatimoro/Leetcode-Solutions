class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
"""All numbers appear twice except for one, find that number"""
