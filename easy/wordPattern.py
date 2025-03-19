class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        ptw = dict()
        wtp = dict()
        s = s.split(' ')
        if len(s) != len(pattern): return False
        for symbol, word in zip(pattern, s):
            if symbol in ptw and ptw[symbol] != word:
                return False
            if word in wtp and wtp[word] != symbol:
                return False
            ptw[symbol] = word
            wtp[word] = symbol
        return True
"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter."""
