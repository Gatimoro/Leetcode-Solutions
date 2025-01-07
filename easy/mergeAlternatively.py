class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        for i,[x,y] in enumerate(zip(word1,word2),start=1):
            ans.append(x)
            ans.append(y)
            top=i
        return ''.join(ans)+max([word1,word2],key=lambda x:len(x))[top:]

"""merge 2 strings alternatively"""
