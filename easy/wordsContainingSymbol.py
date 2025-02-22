class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i,word in enumerate(words):
            if x in word:
                ans.append(i)
        return ans
"""Find all indices of words where words[index] contains a symbol x"""
