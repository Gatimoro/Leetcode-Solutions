class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n, cur = 1, 0
        seen = set()
        
        while cur not in seen:
            seen.add(cur)
            cur *= 10
            cur += 1
            cur %= k
            if not cur:
                return n
            n += 1
        return -1
