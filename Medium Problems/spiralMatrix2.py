class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matty = [[0] * n for _ in range(n)]
        direction = [(-1,0),(0,1),(1,0),(0,-1)]
        count, change, d = 0, n, 1
        i, j = 0, 0
        gearchange = True
        for x in range(1,n**2+1):
            matty[i][j] = x
            count+=1
            if count == change:
                d=(d+1)%4
                count=0
                if gearchange:change-=1
                gearchange=not gearchange
            i+=direction[d][0]
            j+=direction[d][1]
        return matty
"""Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order."""
