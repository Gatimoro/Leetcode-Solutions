class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0
        i = 0
        ans = []

        for index, p in enumerate(s):
            
             
            if p=='(':
                open += 1
                if open != 1:
                    ans.append(p)
            else:
                open -= 1
                if open != 0:
                    ans.append(p)
            
        return ''.join(ans)
