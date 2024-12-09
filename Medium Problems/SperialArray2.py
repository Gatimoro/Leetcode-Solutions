class Solution:"""This week's problem have been tough, it's taking me hours to come up with the algorithms and since everyone is copying the solution i am getting a discouraging runtime"""
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        nums=[x%2 for x in nums]
        queries=[[a[1][0],a[1][1],a[0]] for a in enumerate(queries)]
        queries.sort()
        bot=0
        baddies=[]
        for crack in range(1,len(nums)):
            if nums[crack]==nums[crack-1]:
                baddies.append(crack)
        top=len(baddies)
        ans=[None]*len(queries)
        for que in queries:
            while bot<top and que[0]>=baddies[bot]:
                bot+=1
            if bot<top and que[1]>=baddies[bot]:
                ans[que[2]]=False
                continue
            else:
                ans[que[2]]=True
        return ans
