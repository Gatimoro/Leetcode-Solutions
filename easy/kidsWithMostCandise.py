class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candyman=max(candies)
        return [amount+extraCandies >= candyman for amount in candies]
