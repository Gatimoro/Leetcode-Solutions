class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        stash = deque([(rows-1, cols-1)])
        grid[rows - 1][cols - 1] = 2
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        while stash:
            x, y = stash.popleft()
            if x==y==0:
                return grid[x][y]-2
            high=grid[x][y]
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if nx == -1 or ny == -1 or nx == rows or ny == cols:
                    continue
                if grid[nx][ny] == 0:
                    stash.appendleft((nx,ny))
                    grid[nx][ny] = high
                if grid[nx][ny] == 1:
                    stash.append((nx,ny))
                    grid[nx][ny] = high + 1
"""You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:
0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.
Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)."""
