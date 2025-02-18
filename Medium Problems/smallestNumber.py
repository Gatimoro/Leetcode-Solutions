class Solution:
    def smallestNumber(self, pattern: str) -> str:
        curr = 1
        line = 0
        top = len(pattern)
        i=0
        ans=[]
        while i < top:
            line = 0
            while i < top and pattern[i] == 'D':
                i+=1
                line+=1
            # print(line,'is line\n', ''.join(ans), 'is ans\n', curr, 'is curr\n')
            for j in range(curr + line , curr , -1):
                ans.append(str(j))
            ans.append(str(curr))
            curr+=line+1
            i+=1
        if pattern[-1] == 'I':
            ans.append(str(curr))
        return "".join(ans)
"""
You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions."""
