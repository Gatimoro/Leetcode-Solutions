class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n,101):
            mult=1
            copy=num
            while num:
                mult*=num%10
                num//=10
            if not mult % t:
                return copy
"""You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t."""
