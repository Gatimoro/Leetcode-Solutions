class Solution(object):
    def canBeIncreasing(self, nums):
        warning=False
        for index in range(1, len(nums)-1):
            if nums[index-1]>=nums[index]:
                if nums[index-2]<nums[index]and warning==False or index==1:
                    warning=True
                else:
                    return False
        return True
