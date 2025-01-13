class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]==1:
            return 0
        dp=[0]*len(obstacleGrid[0])
        dp[0]=1
        
        for row in range(len(obstacleGrid)):
            dp[0] = dp[0] if not obstacleGrid[row][0]==1 else 0
            for col in range(1,len(obstacleGrid[0])):
                if obstacleGrid[row][col]==1:
                    dp[col] = 0
                else:
                    dp[col]=dp[col-1]+dp[col]
        return dp[-1]
"""You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109."""
