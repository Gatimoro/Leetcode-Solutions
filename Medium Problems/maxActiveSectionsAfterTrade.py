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
