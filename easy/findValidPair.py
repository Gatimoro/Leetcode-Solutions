class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for a,b in pairwise(s):
            if a==b:
                continue
            if count[a]==int(a) and count[b]==int(b):return a+b
        return ''
"""You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:

The first digit is not equal to the second.
Each digit in the pair appears in s exactly as many times as its numeric value.
Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return an empty string."""
