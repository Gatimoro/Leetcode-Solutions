class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lettas=set([])
        top=0
        start=0
        end=0
        for letta in s:
            end+=1
            while letta in lettas:
                lettas.remove(s[start])
                start+=1
            else:
                top=max(end-start,top)
            lettas.add(letta)
        return(top)
"""Description:
Given a string s, find the length of the longest 
substring
 without repeating characters."""
