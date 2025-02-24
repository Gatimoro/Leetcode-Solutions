class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        cands = []
        if k == 0:
            return 0
        for row, top in zip(grid,limits):
            cands+=sorted(row,reverse=True)[:top]
        cands.sort(reverse=True)
        return sum(cands[:k])
"""You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k. The task is to find the maximum sum of at most k elements from the matrix grid such that:

The number of elements taken from the ith row of grid does not exceed limits[i].

Return the maximum sum"""
