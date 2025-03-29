class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        end = 0
        initial = s.count('1')
        s = '1' + s + '1'
        
        unswitched = 0
        while  end < len(s) and s[end] == '1':
            end += 1
        while  end < len(s) and s[end] == '0':
            end += 1
        while  end < len(s) and s[end] == '1':
            unswitched += 1
            end += 1
        if end == len(s):
            return initial
        start = 0
        while  end < len(s) and s[end] == '0':
            end += 1
        while start < len(s) and s[start] == '1':
            start+=1
        maxi = 0
        
        while start<len(s):
            maxi = max(maxi,end - start - unswitched)
            unswitched = 0
            while  end < len(s) and s[end] == '1':
                unswitched += 1
                end += 1
            while  end < len(s) and s[end] == '0':
                end += 1
            while  start < len(s) and s[start] == '0':
                start += 1
            while  start < len(s) and s[start] == '1':
                start += 1
        return initial + maxi
"""You are given a binary string s of length n, where:

'1' represents an active section.
'0' represents an inactive section.
You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

"""
