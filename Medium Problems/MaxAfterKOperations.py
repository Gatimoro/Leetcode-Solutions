class Solution(object): # AFTER A WHOLE DAY OF LEETCODE NOT ACCEPTING MY SOLUTIONS BECAUSE OF RUNTIME...
    def maxKelements(self, nums, k):  #OR STRAIGHT UP WRONG ANSWERS...
        """
        :type nums: List[int]        #BY JUST INSERTING SORT INSIDE THE WHILE LOOP I BEAT 100%!!!!!!
        :type k: int
        :rtype: int
        """
        
        tot=0
        leg=len(nums)
        nums=sorted(nums)[::-1]
        while k:
            n=1
            tot+=nums[0]
            if nums[0]%3:
                nums[0]=nums[0]//3+1
            else:
                nums[0]=nums[0]//3
            while n<k and n<leg and nums[n]>=nums[0]:
                tot+=nums[n]
                if nums[n]%3:
                    nums[n]=nums[n]//3+1
                else:
                    nums[n]=nums[n]//3
                n+=1
            k-=n
        return tot
