class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                stac=deque([(row,col)])
                cur=grid[row][col]
                grid[row][col]=0
                while stac:
                    r,c=stac.popleft()
                    if r!=0 and grid[r-1][c]!=0:
                        stac.append((r-1,c))
                        cur+=grid[r-1][c]
                        grid[r-1][c]=0
                    if c!=0 and grid[r][c-1]!=0:
                        stac.append((r,c-1))
                        cur+=grid[r][c-1]
                        grid[r][c-1]=0
                    if c!=len(grid[0])-1 and grid[r][c+1]!=0:
                        stac.append((r,c+1))
                        cur+=grid[r][c+1]
                        grid[r][c+1]=0
                    if r!=len(grid)-1 and grid[r+1][c]!=0:
                        stac.append((r+1,c))
                        cur+=grid[r+1][c]
                        grid[r+1][c]=0
                if cur>ans:ans=cur
        return ans
"""You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 """
