class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        next_biggest = list(reversed(list(accumulate(reversed(nums),max))))
        biggest_seen = nums[0]
        ans = 0
        for n in range(1,len(nums)-1):
            ans = max(ans, (biggest_seen - nums[n]) * next_biggest[n+1])
            biggest_seen = max(biggest_seen, nums[n])
        return ans
"""You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

"""
