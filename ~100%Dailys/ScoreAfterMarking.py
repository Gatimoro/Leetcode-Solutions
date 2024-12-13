class Solution:
    def findScore(self, nums: List[int]) -> int:
        score=0
        valid=True
        descend=[]
        """Strategy: when we traverse the array, notice how when we reach a trough (a number less than the previous and greater than the next) it is a guarantee that we will add it. 
        If the numbers keep climbing up we will simply alternate between adding them or not. If we are going down, we will add them to an array, flip it and essentially do the same. 
        This with some minor corrections after the for loop is the crux of my strategy"""
        for x in range(len(nums)-1):
            if valid:
                if nums[x+1]>=nums[x]:
                    if descend:
                        score+=sum(descend[-2::-2])
                        descend=[]
                    score+=nums[x]
                    valid=False
                    continue
                descend.append(nums[x])
            valid=True
        if descend:
            score+=sum(descend[-2::-2])+nums[-1]
        elif valid:
            score+=nums[-1]
        return score
"""Problem: You are given an array nums consisting of positive integers.

Starting with score = 0, apply the following algorithm:

Choose the smallest integer of the array that is not marked. If there is a tie, choose the one with the smallest index.
Add the value of the chosen integer to score.
Mark the chosen element and its two adjacent elements if they exist.
Repeat until all the array elements are marked.
Return the score you get after applying the above algorithm."""
