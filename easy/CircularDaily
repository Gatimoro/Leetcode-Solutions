class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words=eval('["'+sentence.replace(' ','","')+'"]')
        for word in range(-1,len(words)-1):
            if words[word][-1]!=words[word+1][0]:
                return False
        return True
