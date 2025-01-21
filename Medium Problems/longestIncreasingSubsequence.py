class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)
        ans=1
        for i, num in enumerate(nums):
            max_found=1
            for prev in range(i):
                if nums[prev]<num and max_found<dp[prev]+1:
                    max_found=dp[prev]+1
            dp[i] = max_found
            if max_found>ans: ans = max_found
        return ans
"""Given an integer array nums, return the length of the longest strictly increasing 
subsequence
"""
