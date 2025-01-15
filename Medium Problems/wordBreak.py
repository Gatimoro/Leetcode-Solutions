class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tocheck=deque([0])
        goal=len(s)
        seen=set()
        while tocheck:
            index = tocheck.pop()
            for word in wordDict:
                end=index+len(word)
                if s[index:end] == word and end not in seen:
                    tocheck.append(end)
                    if tocheck[-1]==goal:
                        return True
                    seen.add(tocheck[-1])
        return False
"""Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation."""
