class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0      #next 0 position, current index
        r=len(nums)-1 #next 2 position
        def zero(index): #check if num==0
            return True if nums[index]==0 else False
        def two(index): #check if num==2
            return True if nums[index]==2 else False
        def swap(i1,i2):#swap and update r and l indices
            nonlocal r
            nonlocal l
            nums[i1], nums[i2] = nums[i2], nums[i1]
            while l<len(nums) and nums[l]==0:
                l+=1
            while r>0 and nums[r]==2:
                r-=1
        #get starting indices
        while l<len(nums) and zero(l):
            l+=1
        while r>0 and two(r):
            r-=1
        i=l
      """the actual program"""
        while i<=r:
            if zero(r) or two(l): #bring the right zero to the left or viceversa
                swap(r,l)
            if l>i: 
                i=l
                continue #check that i<=r
            #trivial swap
            if zero(i):#bring zero toleft
                swap(l,i)
            elif two(i):#bring two to right
                swap(r,i)
            i+=1
        return nums
"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function."""
