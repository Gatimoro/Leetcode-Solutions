class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        valrow,valcol=[0]*len(grid),[0]*len(grid[0])
        tocheck=deque()
        ans=0
        for i,row in enumerate(grid): valrow[i]=sum(row)
        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col]:
                    valcol[col] += 1
                    tocheck.append((row,col))
        for r, c in tocheck:
            if valrow[r]>=2 or valcol[c]>=2:
                ans+=1
        return ans
"""You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server."""
