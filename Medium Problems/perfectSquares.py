class Solution:
    def numSquares(self, n: int) -> int:
        if n<4:
            return n
        shortest=[float('inf')] * (n+1)
        top=isqrt(n)
        square = 1
        squares=[]
        for odd in range(3,2*top,2):
            square += odd
            squares.append(square)
        for square in reversed(squares):
            shortest[square]=1
            for i in range(1,n+1-square):
                if shortest[i]+1<shortest[i+square]:shortest[i+square]=shortest[i]+1
        for i in range(1,n+1):
            if shortest[i]>shortest[i-1]+1:shortest[i]=shortest[i-1]+1
        return shortest[-1]
"""Return the least amount of perfect squares needed to sum up exacly n"""
