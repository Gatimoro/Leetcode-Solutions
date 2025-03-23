class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        properties = list(map(set, properties))
        def intersect(a,b):
            return len(a & b)
        cons = [[] for _ in range(len(properties))]
        for i in range(len(properties)):
            for j in range(i+1, len(properties)):
                if intersect(properties[i], properties[j]) >= k:
                    cons[i].append(j)
                    cons[j].append(i)
        seen = [False] * len(properties)
        ans = 0
        for node in range(len(properties)):
            
            if seen[node]:
                continue
            ans+=1
            next = [node]
            seen[node] = True
            while next:
                cur = next.pop()
                for n in cons[cur]:
                    if seen[n]:
                        continue
                    seen[n] = True
                    next.append(n)
        return ans
"""You are given a 2D integer array properties having dimensions n x m and an integer k.

Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.

Construct an undirected graph where each index i corresponds to properties[i]. There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.

Return the number of connected components in the resulting graph."""
