class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2)>len(str1):
            return False
        posible=[[ord(x)-97,(ord(x)-98)%26] for x in str2]
        for char in str1:
            if ord(char)-97 in posible[0]:
                posible.pop(0)
                if not posible:
                    return True
        return False 
