class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def g(i, j): (grid[i].__setitem__(j, 0), [g(x, y) for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1))]) if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 else None
        (g(i,j) for i in (range(0,len(grid))) for j in range(len(grid[0])) if i==0 or j==0 )
        return sum([sum(row) for row in grid])
"""You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 """
