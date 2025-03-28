"""You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer."""
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        indices = [(amount, index) for index, amount in sorted(enumerate(queries),key=lambda x: x[1])]
        directions = [(0,1), (-1,0),(1,0),(0,-1)]
        seen = 0
        #queries will be the holder for the answer. I will just update it with the scores.
        
        edges = [(0,0)]
        to_visit = deque([])
        #visited cells shall become 0
        m, n = len(grid), len(grid[0])
        minext = 0
        for max_allowed, corresponding_index in indices:
            if max_allowed <= minext:
                queries[corresponding_index] = seen
                continue
            to_visit = deque(edges)
            edges=set()
            minext=float('inf')
            while to_visit:
                x, y = to_visit.pop()
                if not grid[x][y]: continue
                if grid[x][y] >=  max_allowed:
                    minext = min(minext, grid[x][y])
                    edges.add((x,y))
                    continue
                grid[x][y] = 0
                seen += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx == -1 or ny == -1 or nx == m or ny == n:
                        continue
                    to_visit.append((nx,ny))
            queries[corresponding_index] = seen
        return queries
