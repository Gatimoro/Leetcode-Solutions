class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans=0
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            left, right = s.find(letter), s.rfind(letter)
            if left!=right:
                ans+=len(set(s[left+1:right]))
        return ans
#This problem was quite hard to code when i did the first version, but after implementing the functions find() and set(), which i didn't know you could just input a string into, simplified my code from 25+ lines to the 6 you see
"""DESC
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde"."""
