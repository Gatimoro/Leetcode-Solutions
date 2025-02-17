class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not(word1 and word2):
            if not word1:
                return len(word2)
            return len(word1)
        lcs = [[0] * len(word2) for _ in range(len(word1))]
        inrow = word2.find(word1[0])
        incol = word1.find(word2[0])

        n=1
        for i in range(len(word2)):
            if i == inrow:
                n=0
            lcs[0][i] = n+i
        
        n=1
        for i in range(len(word1)):
            if i == incol:
                n=0
            lcs[i][0] = i+n
        
        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i]==word2[j]:lcs[i][j] = lcs[i-1][j-1]
                else: lcs[i][j] = min(lcs[i][j-1],lcs[i-1][j],lcs[i-1][j-1])+1

        return lcs[-1][-1]

"""Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character"""
