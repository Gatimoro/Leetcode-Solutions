class Solution:
    def smallestPalindrome(self, s: str) -> str:
        half = "".join(sorted(s[:len(s)//2]))
        if len(s)%2: return half + s[len(s)//2] + half[::-1]
        return half + half[::-1]
"""You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

"""
