class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0:
            while True:
                if n==1: return True
                if n&1==1: return False
                n>>=1
        else:
            return False
"""Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x."""
