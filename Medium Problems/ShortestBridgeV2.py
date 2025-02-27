class Solution: """THIS got 99.9% because of the scan abusing the n<=100 constraint"""
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
        found = False
        row,col=random.randint(0,n-1), random.randint(0,n-1)
        while grid[row][col] == 0:
            row,col=random.randint(0,n-1), random.randint(0,n-1)
        grid[row][col] = -1
        q1 = deque([(row,col)])
        q2 = deque()
        ans = 1
        while q1:
            x, y = q1.pop()
            for nx, ny in [(x+1, y),(x-1, y),(x,y+1),(x,y-1)]:
                if nx==-1 or ny==-1 or nx==n or ny==n or grid[nx][ny] == -1:
                    continue
                if grid[nx][ny] == 0:
                    q2.appendleft((nx,ny))
                else:
                    q1.append((nx,ny))
                grid[nx][ny] = -1
        while q2:
            for _ in range(len(q2)):
                x, y = q2.popleft()
                for nx, ny in [(x+1, y),(x-1, y),(x,y+1),(x,y-1)]:
                    if nx==-1 or ny==-1 or nx==n or ny==n or grid[nx][ny] == -1:
                        continue
                    if grid[nx][ny] == 1:
                        return ans
                    q2.append((nx,ny))
                    grid[nx][ny] = -1
            ans+=1
"""You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands."""
