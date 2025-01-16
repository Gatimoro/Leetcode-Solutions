"""You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3."""
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        if len(nums2)%2==1:
            for num in nums1:
                ans^=num
        if len(nums1)%2==1:
            for num in nums2:
                ans^=num
        return ans
