class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26
        if len(s)!=len(t):
            return False
        for l1,l2 in zip(s,t):
            count[ord(l1)-97]-=1
            count[ord(l2)-97]+=1
        for x in count:
            if x:
                return False
        return True
