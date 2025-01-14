class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        ans=0
        bums=set(nums)
        for x in bums:
            if x-1 not in bums:
                count=1
                while x+1 in bums:
                    count+=1
                    x+=1
                if count>ans:
                    ans=count
        return ans
"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""
