class Solution:#this is not an optimal solution but it's mine :)
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid),len(grid[0]) 
        new={(0,0)}
        old=set()
        while new:
            old,new=new,old
            for r,c in old:
                prev=[]
                if c-1>=0:
                    prev.append(grid[r][c-1])
                if r-1>=0:
                    prev.append(grid[r-1][c])
                grid[r][c]+=min(prev)if prev else 0
                if c+1<C:
                    new.add((r,c+1))
                if r+1<R:
                    new.add((r+1,c))
            old.clear()
        return grid[-1][-1]
"""Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time."""
