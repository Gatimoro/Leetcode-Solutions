class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
        normal=sum([abs(a-b) for a, b in zip(arr,brr)])
        brr.sort()
        arr.sort()
        switched=k+sum([abs(a-b) for a, b in zip(arr,brr)])
        return min(normal,switched)
"""
3424. Minimum Cost to Make Arrays Identical
Solved
Medium

You are given two integer arrays arr and brr of length n, and an integer k. You can perform the following operations on arr any number of times:

Split arr into any number of contiguous subarrays and rearrange these subarrays in any order. This operation has a fixed cost of k.
Choose any element in arr and add or subtract a positive integer x to it. The cost of this operation is x.

Return the minimum total cost to make arr equal to brr.

A subarray is a contiguous non-empty sequence of elements within an array."""
