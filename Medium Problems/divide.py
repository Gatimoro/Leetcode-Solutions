class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = -1 if dividend > 0 > divisor or divisor > 0 > dividend else 1
        dividend, divisor = abs(dividend), abs(divisor)
        l, r = 0, dividend
        while l<r:
            m = (l + r + 1) >> 1
            if m * divisor > dividend:
                r = m - 1
            else:
                l = m
        if l * sign < - 2**31:
            return - 2**31
        if l * sign > 2**31 - 1:
            return 2**31 - 1
        return l * sign
"""divide without division"""
