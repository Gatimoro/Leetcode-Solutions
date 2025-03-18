"""somehow this solution got 99.6%"""
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
"""A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days."""
