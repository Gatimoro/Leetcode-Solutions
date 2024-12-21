class Solution:
    def countVowelStrings(self, n: int) -> int:
        sums=deque([[1,2,3,4,5]])
        for i in range(n-1):
            sums.append([sums[-1][0]])
            for j in sums[-2][1:]:
                sums[-1].append(j+sums[-1][-1])
        return sums[-1][-1]
"""Description:
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
"""
