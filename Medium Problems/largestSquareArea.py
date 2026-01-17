# There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

# You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

 
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ansa = 0
        for i,((x1, y1), (x2, y2)) in enumerate(zip(bottomLeft, topRight), start = 1):
            for (x3, y3), (x4, y4) in zip(bottomLeft[i:], topRight[i:]):
                left = max(x1, x3)
                bot = max(y1, y3)
                right = min(x2, x4)
                top = min(y2, y4)
                # print(left, bot, right, top)
                side_length = max(min(right - left, top - bot), 0)
                ansa = max(ansa, side_length)
                # print(ansa)
        return ansa ** 2
        
