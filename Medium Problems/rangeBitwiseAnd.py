class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        prov=left & right
        probe=right-left
        shifts=0
        while probe:
            shifts+=1
            probe>>=1
        return prov>>shifts<<shifts
"""Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive."""
