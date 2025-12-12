class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        palindromes = []
        p = 1
        for i in range(1,128):
            s = str(bin(i))[2:]
            fir, sec = s + s[::-1], s[:-1] + s[::-1]
            palindromes.append(int(fir, 2))
            palindromes.append(int(sec, 2))
            # print(fir, sec)
        ans = [0] * len(nums)
        # print(palindromes)
        for i in range(len(nums)):
            ans[i] = min(abs(pali-nums[i]) for pali in palindromes)
        return ans
