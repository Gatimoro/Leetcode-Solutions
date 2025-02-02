class Solution:
    def maxDifference(self, s: str) -> int:
        vals = sorted(Counter(s).values())
        even=None
        odd=None
        for x in vals:
            if not even and x%2==0:
                even = x
            elif x%2: odd=x
        return(odd-even)
"""You are given a string s consisting of lowercase English letters. Your task is to find the maximum difference between the frequency of two characters in the string such that:

One of the characters has an even frequency in the string.
The other character has an odd frequency in the string.
Return the maximum difference, calculated as the frequency of the character with an odd frequency minus the frequency of the character with an even frequency."""
