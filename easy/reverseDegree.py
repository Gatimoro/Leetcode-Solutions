class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            rev = 123 - ord(s[i])
            ans += rev * (i + 1)
        return ans
