class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for count in Counter(nums).values():
            if count % 2 == 1:
                return False
        return True
"""You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.""'
