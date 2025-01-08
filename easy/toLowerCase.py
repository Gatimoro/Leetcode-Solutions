class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=[]
        for letter in s:
            order=ord(letter)
            if 65<=order<=90:
                ans.append(chr(order+32))
            else:
                ans.append(letter)
        return ''.join(ans)
