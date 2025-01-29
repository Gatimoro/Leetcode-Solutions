class Solution:
    def subsets(self, nums: List[int],cur=[]) -> List[List[int]]:
        top = 1<<len(nums)
        ansa = []
        for bingo in range(top):
            i=0
            comb=[]
            while bingo:
                if bingo & 1 == 1:
                    comb.append(nums[i])
                i+=1
                bingo>>=1
            ansa.append(comb)
        return ansa
"""generate all subsets from nums"""
