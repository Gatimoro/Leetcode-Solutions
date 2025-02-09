class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        ans=0
        leng = len(nums)
        for ind in range(leng):
            ans+=ind - pairs[nums[ind]-ind]
            pairs[nums[ind]-ind]+=1
        return  ans
"""You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums."""
