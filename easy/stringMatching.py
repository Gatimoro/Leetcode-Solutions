class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=set()
        for start, firword in enumerate(words, start=1):
            for secword in words[start:]:
                if  secword in firword:
                    ans.add(secword)
                elif firword not in ans and firword in secword:
                    ans.add(firword)
        return list(ans)
"""desc:
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string"""
