class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = [tuple(word) for word in wordList]  
        words = set(wordList) 
        end=tuple(endWord)#I made everything a tuple so that it runs faster.
        if end not in words:
            return 0
        q = deque([(tuple(beginWord), 2)]) 
        while q:
            word, n = q.popleft()
            for index in range(len(word)):
                for letter in ascii_lowercase:#take every possible letter
                    new = list(word)  # Create a mutable copy
                    new[index] = letter#iInsert new letter
                    new = tuple(new)  # Convert back to a tuple
                    
                    if new in words:#only continue checking 'valid' words.
                        if new == end: return n
                        q.append((new, n + 1))
                        words.remove(new)
        return 0
"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""
