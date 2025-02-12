class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        bysum = defaultdict(lambda: [0, 0]) #store the 2 highest values for each digit sum
        complete = set()
        ans=-1
        for num in nums:
            copy = num
            digi = 0
            while copy:#convert to digit sum and store as digi
                digi += copy%10
                copy //= 10
            i = 0 if bysum[digi][0]<=bysum[digi][1] else 1 #index if the lower value in bysum[digi]
            if bysum[digi][i] < num:
                bysum[digi][i] = num
                if i==1:complete.add(digi) #if num>digi[i], and i==1, it means that we already have 2 values with the same digit sum, so add them to complete for checking
        
        for digi in complete: #now check every complete pair of values and find the greatest one.
            ans = max(ans,sum(bysum[digi]))
        return ans
"""You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions."""
