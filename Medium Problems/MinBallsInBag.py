class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        ori=len(nums)
        baka=max(nums)
        jump=guess=baka-(baka>>1)
        up=0
        if ori == 1:
            maxOperations+=1
            return nums[0]%maxOperations and 1+nums[0]//maxOperations or nums[0]//maxOperations
        while guess>0:
            jump-=jump>>1
            tuti=index=0
            while index<ori and tuti<=maxOperations:
                if nums[index]>guess:
                    tuti+=nums[index]%guess and nums[index]//guess or -1+ nums[index]//guess
                index+=1
            if up and (tuti<=maxOperations and up==1 or tuti>maxOperations and up==-1):
                return up==1 and guess or guess+1
            elif tuti==maxOperations:
                jump=1
            if jump==1 and not up:
                up=tuti>maxOperations and 1 or -1
            guess+=tuti>maxOperations and jump or -jump
        return 1
        
