class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        stack = deque()
        heights = [[-1] * len(isWater[0]) for _ in range(len(isWater))]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    stack.append((0,i,j))
                    heights[i][j] = 0
        while stack:
            height, i, j = stack.popleft()
            for nx, ny in ((1+i ,j),(i,1+j),(i-1,j),(i,j-1)):
                if -1 == nx or nx == len(isWater) or -1 == ny or ny == len(isWater[0]) or heights[nx][ny] != -1:
                    continue
                stack.append((height+1,nx,ny))
                heights[nx][ny]=height+1
        return heights
"""You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them."""
