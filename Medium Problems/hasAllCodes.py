# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = [False] * (1 << k)
        end = k
        for start in range(len(s) - k + 1):
            found[int(s[start:end], 2)] = True
            end+=1
        return all(found)
