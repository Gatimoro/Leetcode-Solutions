class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return [word for word in words if '$'.join(words).count(word)>=2]
      """return the words that are a substring of other words"""
