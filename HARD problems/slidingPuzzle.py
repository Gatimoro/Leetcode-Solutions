class Solution:

    def slidingPuzzle(self, board):
        
       

        def encode(signal):
            s = 1
            tot = 0
            for i in range(2):
                for j in range(3):
                    tot+=signal[i][j] * s
                    s<<=3
            return tot
        solved = encode([[1,2,3],[4,5,0]])
        def decode(signal):
            ret = [[0,0,0],[0,0,0]]
            zpos = None
            for i in range(2):
                for j in range(3):
                    ret[i][j] = signal % 8
                    if not ret[i][j]:
                        zpos = (i,j)
                    signal >>=3
            return ret, zpos
        start = encode(board)
        if start == solved:
            return 0
        stack = deque([start])
        
        moves = 1 
        seen = set([start])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while stack:
            for _ in range(len(stack)):
                board, (zx, zy) = decode(stack.popleft())
                for dx, dy in directions:
                    nx, ny = zx + dx, zy + dy
                    if nx == -1 or ny == -1 or nx == 2 or ny == 3:
                        continue
                    board[zx][zy], board[nx][ny] = board[nx][ny], board[zx][zy] 
                    
                    value = encode(board)
                    if value == solved: 
                        return moves
                    if value not in seen:
                        stack.append(value)
                        seen.add(value) 
                    board[zx][zy], board[nx][ny] = board[nx][ny], board[zx][zy] 
            moves+=1
        return -1 
"""On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1."""
