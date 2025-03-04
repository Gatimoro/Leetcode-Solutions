class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        div = 1
        while div <= n:
            div*=3
        while div:
            div//=3
            if div<=n:
                n-=div
        return n==0
"""Check if a number can be represented as a sum of powers of 3"""
