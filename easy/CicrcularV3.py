class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words=sentence.split()
        for word in range(len(words)-1):
            if words[word][-1]!=words[word+1][0]:
                return False
        return words[0][0]==words[-1][-1]
        
