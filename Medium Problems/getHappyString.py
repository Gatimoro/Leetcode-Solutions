class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_combs =  2 ** (n-1)
        if k>total_combs * 3:
            return ''
        last = ((k-1)//total_combs)+97
        k %= total_combs
        total_combs//=2 
        ans=[chr(last)]
        for _ in range(n-1):
            match last:
                case 97:
                    ud=(98,99)
                case 98:
                    ud=(97,99)
                case 99:
                    ud=(97,98)
            last = ud[(k-1)//total_combs]
            ans.append(chr(last))
            k %= total_combs
            total_combs //= 2
        return ''.join(ans)
"""A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n."""
