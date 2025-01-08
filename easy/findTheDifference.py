class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count=[0]*26
        count[ord(t[-1])-97]=1
        for l1,l2 in zip(s,t):
            count[ord(l1)-97]-=1
            count[ord(l2)-97]+=1
        return ascii_lowercase[count.index(1)]
