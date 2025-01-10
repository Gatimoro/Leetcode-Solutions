class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        track=Counter()
        ans=[]
        for word in words2:
            for letter in set(word):
                track[letter] = max(track[letter], word.count(letter))
        for word in words1:
            found=True
            for letter in track:
                if track[letter] > word.count(letter):
                    found=False
                    break
            if found:
                ans.append(word)
        return ans
"""You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order."""
