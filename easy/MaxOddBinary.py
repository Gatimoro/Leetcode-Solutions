class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s=list(reversed(sorted(s)))
        ln=-1
        while s[ln]=='0':
            ln-=1
        s[ln]='0'
        s[-1]='1'
        return ''.join(s)
"""Finds max odd binary digit by rearranging the digits""
