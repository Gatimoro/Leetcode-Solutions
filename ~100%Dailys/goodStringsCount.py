class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        combs= [1]+[0]*(high) #create an array with the number of combinations for each remaining length
        for i in range(1, high+1):
            combs[i] = (combs[i- zero] +combs[i - one])%1000000007#add the sum of the combinations if the first number is a zero and if it is a one
        return sum(combs[low:high + 1]) % 1000000007
"""DESCRIPTION:
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7."""
