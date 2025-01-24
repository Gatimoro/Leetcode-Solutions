class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        leng=len(nums)
        fir = 0
        last = 0
        forward = list(accumulate(nums,max))
        backward = list(accumulate(reversed(nums),min))
        
        for a,b in zip(forward,reversed(backward)):
            if a!=b:
                break
            leng-=1
        
        if leng==0:
            return 0
        
        for a,b in zip(reversed(forward),backward):
            if a!=b:
                break
            leng-=1
        
        return leng
"""Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length."""
