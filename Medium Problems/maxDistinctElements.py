# You are given an integer array nums and an integer k.

# You are allowed to perform the following operation on each element of the array at most once:

# Add an integer in the range [-k, k] to the element.
# Return the maximum possible number of distinct elements in nums after performing the operations.


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        count = 0
        last_used = -k
        for num in sorted(nums):
            if last_used < num - k:
                last_used = num - k
                count += 1
            elif num - k <= last_used < num + k:
                last_used += 1;
                count += 1
        return count
