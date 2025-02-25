class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        evens,odds = 1,0
        ans = 0
        bum=0
        currently_odd = False
        for itsOdd in arr:
            bum+=itsOdd
            bum%=2
            if bum:
                ans += evens
                odds += 1
            else:
                ans += odds
                evens += 1

        return  ans%1000000007
"""Return the amount of odd sum subarrays"""
