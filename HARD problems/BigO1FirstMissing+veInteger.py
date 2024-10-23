class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]          THIS TOOK UNNECESSARILY LONG BUT IT'S MY 
        :rtype: int                 FIRST BIG O PROBLEM AND I'M HAPPY THAT I GOT IT :}
        """
        sort=hold=0
        leg=len(nums)
        while sort<leg:
            num=nums[sort]
            if nums[sort]!=sort+1:
                nums[sort]=0
                while 0<num<=leg:
                    if nums[num-1]==num:
                        break

                    hold=nums[num-1]#save the tile we'll fill to hold
                    nums[num-1]=num #reassign it's value to it's index +1
                    num=hold        #repeat while hold is inside      
            sort+=1
        return (nums+[0]).index(0)+1 #correct the output
