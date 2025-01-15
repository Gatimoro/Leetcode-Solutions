class Solution:
    def hammingWeight(self, n: int) -> int:
        return 0 if n==0 else (1&n) + self.hammingWeight(n>>1)
