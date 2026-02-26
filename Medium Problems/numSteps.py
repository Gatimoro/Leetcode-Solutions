# Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

# If the current number is even, you have to divide it by 2.

# If the current number is odd, you have to add 1 to it.

# It is guaranteed that you can always reach one for all test cases.
class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s,2)
        ansa = 0
        while num > 1:
            if num & 1:
                num += 1                
            else:
                num >>= 1
            ansa += 1
        return ansa
