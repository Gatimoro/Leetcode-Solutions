class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        difs=Counter(nums)
        ans=0
        for num in difs:
            if num-1 not in difs:
                last=num*difs[num]
                prelast=0
                while num+1 in difs:
                    num+=1
                    prelast, last = last, max(last, prelast + num*difs[num])
                ans+=last
        return ans
"""You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times."""
