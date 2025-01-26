class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<r:
            m=(l+r+1)//2
            square = m*m
            if square < x: l = m
            elif square > x: r = m - 1
            else:return m
        return l
"""integer square root"""
