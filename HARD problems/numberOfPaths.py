You are given a 0-indexed m x n integer matrix grid and an integer k. You are currently at position (0, 0) and you want to reach position (m - 1, n - 1) moving only down or right.

Return the number of paths where the sum of the elements on the path is divisible by k. Since the answer may be very large, return it modulo 109 + 7.

 
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        ways =[[[0]*k for _ in grid[0]] for _ in grid]
        ways[0][0][grid[0][0] % k] = 1
        MOD = 1_000_000_007
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                # print(i,j)
                # print(ways)
                if i > 0:
                    for idx, prev_sum in enumerate(ways[i-1][j]):
                        ways[i][j][(idx + num) % k] += prev_sum
                        ways[i][j][(idx + num) % k] %= MOD
                if j > 0:
                    for idx, prev_sum in enumerate(ways[i][j-1]):
                        # print(i,j,num)
                        ways[i][j][(idx + num) % k] += prev_sum
                        ways[i][j][(idx + num) % k] %= MOD
        return ways [-1][-1][0]
