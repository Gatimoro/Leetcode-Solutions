class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = set()
        ans = 0
        def investigate(prov):
            for neighbor in range(size):
                if isConnected[prov][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    investigate(neighbor)
        for i in range(size):
            if i not in visited:
                ans+=1
                investigate(i)
        return ans
"""There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces."""
