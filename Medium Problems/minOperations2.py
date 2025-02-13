class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        c=0
        while nums[0]<k:
            heappush(nums,heappop(nums)*2+heappop(nums))
            c+=1
        return c
"""You are given a 0-indexed integer array nums, and an integer k.

You are allowed to perform some operations on nums, where in a single operation, you can:

Select the two smallest integers x and y from nums.
Remove x and y from nums.
Insert (min(x, y) * 2 + max(x, y)) at any position in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k."""
