class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        start, end, cum = 0, 0, 0
        topLen = 0
        currentLen = 0
        while end < len(nums):
            # if can't add to seq, chop up the tail
            if cum & nums[end]:
                cum ^= nums[start]
                start += 1
                currentLen -= 1
            else:
                cum |= nums[end]
                end+=1
                currentLen+=1
                if currentLen>topLen:
                    topLen += 1
        return topLen
"""You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice."""
