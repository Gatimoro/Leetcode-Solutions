class Solution:
    def maxScore(self, s: str) -> int:
        cur=s.count("1")
        top=0
        for letter in s[:-1]:
            if letter=="0":
                cur+=1
            else:
                cur-=1
            top=max(top,cur)
        return top
"""Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring."""
