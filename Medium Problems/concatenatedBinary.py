class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        ans = 0
        shift = 1
        for cur in range(1, n+1):
            if cur == 1<<shift:
                shift += 1
            ans <<= shift
            ans += cur
            ans %= 1000000007
            if cur == 1<<shift:
                shift += 1
            #print(ans)
        return ans
