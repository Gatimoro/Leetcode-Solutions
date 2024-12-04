class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        search=ord(str2[0])
        n=0
        lim=len(str2)
        for char in str1:
            num=ord(char)
            if num==search or num==search-1 or num==122 and search==97:
                n+=1
                print(n)
                if n==lim:
                    return True
                search=ord(str2[n])
        return False 
