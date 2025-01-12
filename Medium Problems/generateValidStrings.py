class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def findnext(arr,length):
            if length==n:
                ans.append(''.join(arr))
                return
            elif arr[-1] == '1':
                findnext(arr+['0'],length+1)
            findnext(arr+['1'],length+1)
        findnext(['1'],1)
        findnext(['0'],1)
        return ans
"""desc:
You are given a positive integer n.

A binary string x is valid if all 
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order."""
