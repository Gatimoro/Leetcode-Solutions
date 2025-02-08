class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        ans=1
        for roll in rolls:
            seen.add(roll)
            if len(seen)==k:
                ans+=1
                seen.clear()
        return ans
"""You are given an integer array rolls of length n and an integer k. You roll a k sided dice numbered from 1 to k, n times, where the result of the ith roll is rolls[i].

Return the length of the shortest sequence of rolls so that there's no such 
subsequence
 in rolls.

A sequence of rolls of length len is the result of rolling a k sided dice len times."""
