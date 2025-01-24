class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return '0'
        sec=(str(b) for b in nums)
        return ''.join(sorted(sec,key= lambda x: x*10, reverse=True))
