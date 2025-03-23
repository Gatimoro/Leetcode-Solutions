class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        bestlen = [ [float('inf'),0] for _ in range(n)]
        cons = [[] for _ in range(n)]
        bestlen[0] = [0,1]
        for a, b, distance in roads:
            cons[a].append((b,distance))
            cons[b].append((a,distance))
        q = [(0,0)]
        heapify(q)
        MOD = (10 ** 9) + 7 
        while q:
            time, intersection = heappop(q)
            
            min_time, ways = bestlen[intersection]
            if intersection == n-1:
                return ways

            for neighbor,distance in cons[intersection]:
                next_time = time + distance
                if next_time > bestlen[neighbor][0]:
                    continue
                if next_time < bestlen[neighbor][0]:
                    bestlen[neighbor] = [next_time, ways]
                    heappush(q, (next_time, neighbor))
                elif next_time == bestlen[neighbor][0]:
                    bestlen[neighbor][1] = (bestlen[neighbor][1] + ways) % MOD 

"""You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7."""
