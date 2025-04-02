class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        next_biggest = list(reversed(list(accumulate(reversed(nums),max))))
        biggest_seen = nums[0]
        ans = 0
        for n in range(1,len(nums)-1):
            ans = max(ans, (biggest_seen - nums[n]) * next_biggest[n+1])
            biggest_seen = max(biggest_seen, nums[n])
        return ans
