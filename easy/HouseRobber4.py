class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(kapa):
            cur = 0
            ans = 1
            for pack in weights:
                cur += pack
                if cur>kapa:
                    ans += 1
                    cur = pack
                    if pack>kapa:
                        return False
            return ans <= days
        l,r = 0, max(weights) * ((len(weights)//days)+1)
        while l<r:
            guess = (l + r ) >>1
            if check(guess):
                r = guess
            else:
                l = guess +1
        return l
"""There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses."""
