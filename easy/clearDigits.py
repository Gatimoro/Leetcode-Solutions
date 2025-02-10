class Solution:
    def clearDigits(self, s: str) -> str:
        def isNum(sym):
            return '9'>=sym>='0'
        symbols=reversed(list(s))
        ans=[]
        skip=0
        for symbol in symbols:
            if isNum(symbol):
                skip+=1
            else:
                if skip:
                    skip-=1
                else:
                    ans.append(symbol)
        return ''.join(ans[::-1])
"""You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits."""
