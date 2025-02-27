class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        mi, mj = len(maze)-1, len(maze[0])-1
        deq = deque()
        maze[entrance[0]][entrance[1]] = 0
        i,j = entrance
        for px, py in [(i+1, j),(i-1,j),(i,j-1),(i,j+1)]:
            if  mi>=px>=0 and mj>=py>=0 and maze[px][py] == '.':
                if px==0 or py==0 or px==mi or py == mj: return 1
                maze[px][py] = (1)
                deq.append((px,py))
        while deq:
            i, j = deq.popleft()
            for nx, ny in [(i+1, j),(i-1,j),(i,j-1),(i,j+1)]:
                if maze[nx][ny] == '.':
                    if nx==0 or ny==0 or nx==mi or ny == mj: return maze[i][j] + 1
                    maze[nx][ny] = (maze[i][j] + 1)
                    deq.append((nx,ny))
        return -1
