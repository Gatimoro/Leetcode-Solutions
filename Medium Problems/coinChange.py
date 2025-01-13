class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*amount #I took an approach not seen in solutions and got 99%!!!
        if amount==0:
            return 0
        
        for coin in reversed(sorted(set(coins))):
            if coin<=amount:
                dp[coin-1]=1
                for multi in range(coin-1,amount-coin): 
                    if dp[multi] !=0 and (dp[multi+coin]>dp[multi]+1 or dp[multi+coin]==0):
                        dp[multi+coin] = dp[multi] + 1
        return dp[amount-1] if dp[amount-1]!=0 else -1
"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin."""
