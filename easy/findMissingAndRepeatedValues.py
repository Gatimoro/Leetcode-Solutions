class Solution:
    def findMissingAndRepeatedValues(self, grid ):
        ans=0
        seen = set()
        n=len(grid)*len(grid)
        f = (n+1)*n//2
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in seen:
                    ans = grid[i][j]
                else:
                    seen.add(grid[i][j])
                    f-= grid[i][j]
            
        
        return [ans, f]
"""There is a value from 1 to n squared that doesn't appear in the matrix and a different value takes it's place, appearing twice. Find these two values"""
