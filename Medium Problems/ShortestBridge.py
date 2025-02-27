class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n=len(grid)
       
        def invalid(i,j):     #check if i,j valid
            if i==-1: return True
            if j==-1: return True
            if i==n: return True
            if j==n: return True
            if grid[i][j] == -1: return True
            return False
  
        def get():          #the index of the first 1
            for row in range(n):
                for col in range(n):
                    if grid[row][col] == 1: return (row,col)
        start = get()
        grid[start[0]][start[1]] = -1
        q1 = deque([start])
        q2 = deque([("$",0)])
        ans = 1
        while q1:
            x, y = q1.pop()
            for nx, ny in ((x+1, y),(x-1, y),(x,y+1),(x,y-1)):
                if invalid(nx,ny):
                    continue
                if grid[nx][ny] == 0:
                    q2.appendleft((nx,ny))
                else:
                    q1.append((nx,ny))
                grid[nx][ny] = -1
        while q2:
            x, y = q2.popleft()
            if x == "$": 
                ans+=1
                q2.append(("$",0))
                continue
            for nx, ny in ((x+1, y),(x-1, y),(x,y+1),(x,y-1)):
                if invalid(nx,ny):
                    continue
                if grid[nx][ny] == 1:
                    return ans
                q2.append((nx,ny))
                grid[nx][ny] = -1
