# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        biggest = 0
        heights += [0]
        stack = []
        for i, h in enumerate(heights):
            po = i
            while stack and stack[-1][0] >= h:
                height, po = stack.pop()
                biggest = max(biggest, (i - po) * height)
            stack.append((h, po))
            # print(stack)
        return biggest
