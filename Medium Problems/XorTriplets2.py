class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set(nums)
        seen = set()
        ans = set()
        for a in s:
            for b in s:
                seen.add(a^b)

        for v in seen:
            for w in s:
                ans.add(v^w)
        return len(ans)

"""You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k)."""
