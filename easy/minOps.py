class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum( 1 for x in nums if x%3)
# You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.

# Return the minimum number of operations to make all elements of nums divisible by 3.

 
