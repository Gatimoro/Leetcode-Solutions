# You are given an integer array nums consisting of unique integers.

# Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

# The smallest and largest integers of the original range are still present in nums.

# Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

# Note: Please do not copy the description during the contest to maintain the integrity of your submissions.
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return [n for n in range(min(nums),max(nums)+1) if n not in set(nums)]
