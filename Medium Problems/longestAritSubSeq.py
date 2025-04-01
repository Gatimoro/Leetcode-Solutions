class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        nnum = [{} for _ in range(len(nums))]
        ans = 2
        for i, num in enumerate(nums):
            for j in range(i):
                diff = num - nums[j]
                nnum[i][diff] = nnum[j].get(diff,1) + 1
                ans = max(nnum[i][diff], ans)

        return ans
"""Find longest arithmetic subesquence in an array."""
