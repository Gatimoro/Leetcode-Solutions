class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        #initialize
        num_keys = 0
        m, n = len(grid), len(grid[0])
        visi = [[[] for _ in range(n)] for _ in range(m)]
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        key_vals, lock_vals = set('abcdef'), set('ABCDEF')

        #helper functions
        def update(count, letter):
            return count | (1<<(ord(letter.upper())-65))
        
        def inKeyChain(count, letter):
            return letter not in lock_vals or count & (1<<(ord(letter)-65)) != 0
        

        #find the amount of keys and locks
        for row in range(m):
            for col in range(n):
                if grid[row][col] in key_vals:
                    num_keys += 1
                elif grid[row][col] == '@':
                    q = deque([(row,col,0,1)])
                    visi[row][col] = [0]
        while q:
            x, y, keys, moves = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                #check if neighbor is valid and not redundant
                if nx == -1 or nx == m or ny == -1 or ny == n or keys in visi[nx][ny] or grid[nx][ny] == '#' or not inKeyChain(keys, grid[nx][ny]):
                    continue
                #add key to keychain
                if grid[nx][ny] in key_vals:
                    nkeys = update(keys,grid[nx][ny])
                    if nkeys == (1<<(num_keys))-1:
                        return moves
                else:
                    nkeys = keys
                #update visi to not visit the same cell with the same keychain again.
                visi[nx][ny].append(nkeys)
                q.append((nx, ny, nkeys, moves+1))
        return -1
"""You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1."""
