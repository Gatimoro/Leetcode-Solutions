class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for num in nums:
            if num != nums[i]:
                i+=1
                nums[i] = num
        return i+1
#goal is to remove the duplicates in place and return the number of different elements from a sorted array
