class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads)==0:return 0
        groph = defaultdict(set)
        for a, b in roads:
            groph[a].add(b)
            groph[b].add(a)
        ans=0
        for i in range(n):
            for j in range(i+1, n):
                ans=max(ans, len(groph[i]) + len(groph[j]) - (i in groph[j]))
        return ans
"""There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure."""
