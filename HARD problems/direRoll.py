class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp=[[[0] * 6 for _ in range(6)] for _ in range(n)]
        #dp[throw number][lastnumber][appeared _ times]
        dp = [[0] * (rollMax[n]) for n in range(6)]
        for ni in range(6):
            if rollMax[ni]:
                dp[ni][0] = 1
        for _ in range(n-1):
            next_layer = [[0] * (rollMax[n]) for n in range(6)]
            #for each possible ending
            tota = sum(sum(row) for row in dp)
            for end in range(6):
                #choose same element
                for cons in range(1,rollMax[end]):
                    next_layer[end][cons] = dp[end][cons - 1]
                next_layer[end][0] = tota - sum(dp[end])
            dp = next_layer

        return sum(sum(row)%1000000007 for row in dp)%1000000007    
"""A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

Two sequences are considered different if at least one element differs from each other.

 """
