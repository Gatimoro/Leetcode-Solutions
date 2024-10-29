class Solution:
    def maxMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        longer = 0
        
        def track(row, col, last):
            nonlocal longer
            if col == n - 1:
                longer = n - 1
            else:
                grid[row][col] = 0 #since we record the furthest reached column, the path is redundand so we make sure not to check twice.
                no = True #have we not found nothing?
                
                #check for valid paths and boundaries. No need to check for col as when we reach n-1 we direcly assign it to longer above.
                if row + 1 < m and grid[row + 1][col + 1] > last:
                    track(row + 1, col + 1, grid[row + 1][col + 1])
                    no = False
                if grid[row][col + 1] > last:
                    track(row, col + 1, grid[row][col + 1])
                    no = False
                if row - 1 >= 0 and grid[row - 1][col + 1] > last:
                    track(row - 1, col + 1, grid[row - 1][col + 1])
                    no = False
                
                if no and col>longer:#when no path forward, check if we reached a new record
                    longer = col
        
        for xnxx in range(m): #this is the only dp we need
            track(xnxx, 0, grid[xnxx][0])
            if longer==n-1:#if we reach the end of the grid we don't have to keep checking
                return n-1
        return longer
