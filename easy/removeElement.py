class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for n in nums:
            if n != val:
                if nums[i] != n:
                    nums[i]=n
                i+=1
        return i
