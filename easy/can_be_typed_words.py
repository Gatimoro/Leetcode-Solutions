#returns how many words from text can be typed withoun using any of the leters from brokenLetters.
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return len(list(filter(lambda w: not ( set(w) & set(brokenLetters) ), text.split(' '))))
