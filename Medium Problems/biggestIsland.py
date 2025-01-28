class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                stac=deque([(row,col)])
                cur=1
                grid[row][col]=0
                while stac:
                    r,c=stac.popleft()
                    if r!=0 and grid[r-1][c]!=0:
                        stac.append((r-1,c))
                        cur+=1
                        grid[r-1][c]=0
                    if c!=0 and grid[r][c-1]!=0:
                        stac.append((r,c-1))
                        cur+=1
                        grid[r][c-1]=0
                    if c!=len(grid[0])-1 and grid[r][c+1]!=0:
                        stac.append((r,c+1))
                        cur+=1
                        grid[r][c+1]=0
                    if r!=len(grid)-1 and grid[r+1][c]!=0:
                        stac.append((r+1,c))
                        cur+=1
                        grid[r+1][c]=0
                if cur>ans:ans=cur
        return ans
"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0."""
