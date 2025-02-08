class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for num in nums:
            if 100 > num > 9 or 10000 > num > 999 or num > 99999: ans+=1
        return ans
"""Given an array nums of integers, return how many of them contain an even number of digits."""
