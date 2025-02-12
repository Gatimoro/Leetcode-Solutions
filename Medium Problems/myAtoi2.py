class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:return 0
        start=0
        sign = 1
        while s[start]==' ':
            start+=1
            if start==len(s):return 0
        
        if s[start] == '+':start+=1
        elif s[start]== '-':
            start+=1
            sign=-1
        ans = 0
        while start<len(s):
            if not '0'<= s[start] <= '9': break
            ans*=10
            ans+=int(s[start])
            if sign==-1 and ans >= 1 << 31: return -(1<<31)
            elif ans >= 1<<31: return (1<<31) -1
            start+=1
        return ans * sign
"""Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 """
