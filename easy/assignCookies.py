class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        g.sort(reverse=True)
        s.sort(reverse=True)
        i = 0
        for child in g:
            if child<=s[i]:
                i+=1
                print(i,len(s))
                if i==len(s):
                    break
        return i
