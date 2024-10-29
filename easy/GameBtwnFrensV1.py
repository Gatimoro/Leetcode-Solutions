import math
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        frens=[0]
        for i in range(2,n):
            frens+=[i]
        m=2
        l=(k+1)%n
        while l in frens:
            frens.remove(l)
            l=(m*k+l)%n
            m+=1
        if 0 in frens:
            frens=frens[1:]+[n]
        return frens
