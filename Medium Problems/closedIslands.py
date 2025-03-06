class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m, n = len(grid), len(grid[0])
        #let's first color the invalid islands
        def color(i,j):
            nonlocal island
            if i==0 or j==0 or i==m-1 or j==n-1:
                island = False
            for dx, dy in directions:
                x, y = i + dx, j + dy
                
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    grid[x][y] = 1
                    color(x,y)
        ans=0
        for row in range(m):
            for col in range(n):
                if not grid[row][col]:
                    grid[row][col] = 1
                    island = True
                    color(row, col)
                    if island:
                        ans+=1
        return ans
"""Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands."""
