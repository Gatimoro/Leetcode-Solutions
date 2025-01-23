"""Intuition and Approach
Our goal is to find the largest square of 1s in a binary matrix. Instead of working directly with a 2D DP table, 
we will simplify the problem by transforming each row of the matrix into a single integer. 
This allows us to use bitwise operations, which are faster and more intuitive in this context.

Think of the matrix as layers of squares stacked on top of each other. The algorithm "squishes" these squares into 
smaller ones layer by layer, merging information about overlapping 1s from adjacent rows.

During this process:

Horizontal adjacency (if there is a 1 next to a 1) is checked using a left-shift and an AND operation (a & (a << 1)).

Vertical adjacency is handled by combining rows with another AND operation (a & b for adjacent rows).

At every step, smaller squares that can no longer form larger squares "disappear," 
and the process continues until no squares remain. The number of iterations (or "squishing steps") represents the side length of the largest square"""

class Solution:"""I am so proud of myself :)"""
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #convert to numbers
        mynums = [int(''.join(row),2) for row in matrix]
        #operate
        ans=0
        while any(mynums):
            mynums = [a & (a<<1) for a in mynums]
            mynums= [a & b for a, b in pairwise(mynums)]
            ans+=1
        return ans*ans
"""description:
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area."""
