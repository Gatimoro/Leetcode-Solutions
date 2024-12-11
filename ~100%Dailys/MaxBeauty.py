class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        count=[0]*(1+max(nums))
        for n in nums:#count how many times does each number appear.
            count[n]+=1
        i=2*k+1
        ans=c=sum(count[:2*k+1])
        while i < len(count):#use a sliding window to find the window with the maximum count sum.
            c=c-count[i-2*k-1]+count[i]
            ans=max(ans,c)
            i+=1
        return ans
