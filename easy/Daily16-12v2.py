class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            m=0
            o=nums[0]
            for i in range(1,len(nums)):
                if nums[i]<o:
                    o=nums[i]
                    m=i
            nums[m]*=multiplier
        return nums
