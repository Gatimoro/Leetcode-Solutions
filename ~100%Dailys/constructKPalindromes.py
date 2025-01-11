class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>=len(s): #we can't split in more parts than symbols. if k == length we can just split in k parts of length 1
            if k==len(s):
                return True
            return False
        for lett in set(s):
            k -= s.count(lett)%2 #the number of palindromes we have is k. When we see an odd count we convert one of the palindromes to even and this palidrome can only be added letters with even count. 
        return k>=0 #k keeps track of how many still even palindromes do we have. If we run out of them, it means that k is too small and we return False.
