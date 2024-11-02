class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=eval('["'+sentence.replace(' ','","')+'"]')
        if sentence[0]!=sentence[-1]:
            return False
        for letter in range(len(sentence)-1):
            if sentence[letter]==' ' and sentence[letter + 1] != sentence[letter - 1]:
                return False
        return True
