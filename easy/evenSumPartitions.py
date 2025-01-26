class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right=sum(nums)
        ans=0
        left=0
        for num in nums[:-1]:
            right-=num
            left+=num
            if (left-right)%2==0:
                ans+=1
        return ans
"""Count partitions with even sum"""
