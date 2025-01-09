class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        def nowcheck(arr,i):
            for num in range(i,len(candidates)):
                hold=[candidates[num]]+arr
                suma=sum(hold)
                if suma<target:
                    nowcheck(hold, num)
                else:
                    if suma==target:
                        ans.append(hold)
                    break
        nowcheck([],0)
        return ans
"""return every combination that adds up to target without repeats."""
