class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        last=nums[0]
        inc, dec = 1, 1
        ans=0
        for num in nums:
            if num>last:
                inc+=1
            else:
                inc=1
            if num<last:
                dec+=1
            else:
                dec=1
            last=num
            ans=max(ans,inc,dec)
        return ans
