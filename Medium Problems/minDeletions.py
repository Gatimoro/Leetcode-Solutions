class Solution:
    def minDeletions(self, s: str) -> int:
        appearences_of_ = Counter(s)
        seen=set()
        ans=0
        for freq in appearences_of_.values():
            while freq in seen:
                freq-=1
                ans+=1
            if freq>0:
                seen.add(freq)
        return ans
"""A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1."""
