class Solution:"""PRICES IS THE PRICES EVERY DAY FOR A PERIOD OF TIME, THE TASK IS TO RETURN THE MAXIMUM PROFIT buying on one day and selling on a future one."""
    def maxProfit(self, prices: List[int]) -> int:
        money,buy=0,prices[0]
        for lera in prices[1:]:
            if lera<buy:
                buy=lera
            elif lera-buy>money:
                money=lera-buy
        return money
