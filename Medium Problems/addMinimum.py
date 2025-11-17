# Given a string word to which you can insert letters "a", "b" or "c" anywhere and any number of times, return the minimum number of letters that must be inserted so that word becomes valid.

# A string is called valid if it can be formed by concatenating the string "abc" several times.
class Solution:
    def addMinimum(self, word: str) -> int:
        abc = ['a','b','c']
        ads = 0
        abi = 0
        i = 0
        while i < len(word):
            l = word[i]
            if l == abc[abi]:
                i += 1
            else:
                ads += 1
            abi += 1
            abi %= 3
        if word[-1] == 'a':
            return ads + 2
        elif word[-1] == 'b':
            return ads + 1
        return ads

class Solution:
    def addMinimum(self, word: str) -> int:
        ads = 0
        i = 0
        while i < len(word):
            for correct in "abc":
                if i < len(word) and word[i] == correct:
                    i += 1
                else:
                    ads += 1
        return ads

class Solution:
    def addMinimum(self, word: str) -> int:
        i = ads = 0
        while i < len(word):
            for correct in "abc": i, ads = (i + 1, ads) if i < len(word) and word[i] == correct else (i, ads + 1)
        return ads
