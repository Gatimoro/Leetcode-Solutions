class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = 0
        n = len(s)
        a, b = 0,0
        for i in range(n):
            l,r = i-1, i+1
            cur = 1
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                cur += 2
                r+=1

            if cur > best:
                best = cur
                a, b = l+1, r
            l,r = i, i + 1
            cur = 0
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                cur += 2
                r+=1

            if cur > best:
                best = cur
                a, b = l+1, r
        return s[a:b]
"""Find longest palindromic substring"""
