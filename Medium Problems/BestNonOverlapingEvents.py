class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans=greatest=0
        #store starts and ends along with their value and an indicator of what they are. 1 for start 0 for end.
        news=sorted([[x[0]-1,1,x[2]] for x in events]+[[x[1],0,x[2]] for x in events])#x[0]-1 so that in case of a tied time between a start and an end, we compute the start first.
        for trip in news:
            if trip[1]:
                ans=max(ans,trip[2]+greatest)
            else:
                greatest=max(greatest,trip[2])
        return ans
        
