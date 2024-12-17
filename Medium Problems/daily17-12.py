class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        i , j = 0 , 0
        zeros = [0] * 26
        ans=''
        for letter in s:
            zeros[-((ord(letter)-122))]+=1
        while i<26:
            if not zeros[i]:
                i+=1
            elif 0<zeros[i] <= repeatLimit:
                ans+=zeros[i]* chr(122-i)
                zeros[i]=0
                i+=1
            else:
                ans+=repeatLimit*chr(122-i)
                zeros[i]-=repeatLimit
                while j<26 and not zeros[j] or j==i:
                    j+=1
                if i==25 or j==26:
                    break
                else:
                    ans+=chr(122-j)
                    zeros[j]-=1
        return ans
"""DESCRIPTION:
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one."""
