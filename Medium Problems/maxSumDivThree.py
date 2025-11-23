# Given an integer array nums, return the maximum possible sum of elements of the array such that it is divisible by three.

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        ans = [0,0,0]
        for n in nums:
            next_ans = ans.copy()
            for pre in ans:
                nex = pre + n
                next_ans[nex % 3] = max(next_ans[nex % 3], nex)
            ans = next_ans
        return ans[0]
