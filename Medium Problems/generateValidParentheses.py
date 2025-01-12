class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(cur,opens,closed):
            if len(cur) == 2*n:
                ans.append(cur)
                return
            if opens<n:
                generate(cur + '(' , opens+1, closed)
            if closed<opens:
                generate(cur + ')' , opens, closed + 1)
        generate('',0,0)
        return ans
"""desc:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""
