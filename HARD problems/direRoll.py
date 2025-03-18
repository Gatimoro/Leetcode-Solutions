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
