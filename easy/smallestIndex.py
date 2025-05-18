class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def s(n):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return ans
        for i,n in enumerate(nums):
            # print(n, s(n))
            if s(n) == i:
                return i
        return -1
# You are given an integer array nums.

# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

# If no such index exists, return -1.
