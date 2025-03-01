class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count=0
        for num in nums:
            count+=(num+1)%2
        return [0] * count + [1]*(len(nums)-count)
"""You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.

 """
