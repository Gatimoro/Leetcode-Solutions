class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        seen={}
        ans=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                prod = nums[i] * nums[j]
                if prod in seen:seen[prod]+=1
                else: seen[prod]=1
        for x in seen.values(): ans+=4*(x*(x-1))
        return ans
"""Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d."""
