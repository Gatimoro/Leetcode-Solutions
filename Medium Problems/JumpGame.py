class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=0
        for num in range(len(nums)-1,-1,-1):  
            if nums[num]>=count:count=0
            count+=1
        return count==1
"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself."""
