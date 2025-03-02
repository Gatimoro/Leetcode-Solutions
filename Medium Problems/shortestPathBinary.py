class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        if grid[0][0] or grid[n-1][n-1]: return -1
        if n==1: return 1
        nomnom = deque([(0,0)]) 
        grid[0][0] = 1
        plas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        level = 1
        while nomnom:
            for e____sk in range(len(nomnom)):
                x, y = nomnom.popleft()                
                for dx, dy in plas:
                    nx, ny = x + dx, y + dy
                    if x == y == n - 1: return level
                    if nx < 0 or ny < 0 or nx == n or ny == n or grid[nx][ny] == 1:
                        continue
                    grid[nx][ny] = 1
                    nomnom.append((nx,ny))
            level += 1
        return -1
""" Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path. """
