class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        for a, b in zip(s1,s2):
            if a!=b:
                count+=1
                if count==1:
                    last=(a,b)
                elif count==2:
                    if last!=(b,a):return False
                else:return False
        return not count%2
