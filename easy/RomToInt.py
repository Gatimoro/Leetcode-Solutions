class Solution:
    def romanToInt(self, s: str) -> int:
        trans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot,max_seen=0,0
        for symbol in reversed(s):
            val=trans[symbol]
            if val<max_seen:tot-=val
            else:tot+=val
            max_seen=max(max_seen,val)
        return tot
"""Converts roman to integer"""
