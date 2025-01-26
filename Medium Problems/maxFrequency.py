"""You are given an array nums of length n. You are also given an integer k.

You perform the following operation on nums once:

Select a 
subarray
 nums[i..j] where 0 <= i <= j <= n - 1.
Select an integer x and add x to all the elements in nums[i..j].
Find the maximum frequency of the value k after the operation."""

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 0
        for val in range(0, 51):
            if val==k:continue
            top, count = 0, 0
            for num in nums:
                if num==val:
                    count += 1
                    if count > top: top = count
                elif num == k and count >= 1:count -= 1
            if top>ans: ans=top
        return ans + nums.count(k)
