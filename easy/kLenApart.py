class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c = float('inf')
        for n in nums:
            c += 1
            # print(c, n)
            if n == 1:
                if c <= k:
                    return False
                c = 0
            
        return True
# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

