class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        
        graph = [[[] for _ in range(n)], [[] for _ in range(n)]]
        for start, finish in redEdges:
            graph[0][start].append(finish)
        for start, finish in blueEdges:
            graph[1][start].append(finish)

        segregated = [False]*(2*n) #[...(n-1)] visited black & [n...] visited white
        stash = deque([(0,0,0),(0,1,0)])
        obscurity = [-1] * n #how hard this friend is to reach
        
        while stash:
            individual, race, depth = stash.popleft()
            #transrace node now associates with a new group of friends
            segregated[race*n + individual]=True
            if obscurity[individual] == -1 or obscurity[individual]>depth:
                obscurity[individual] = depth
            race += 1
            race %= 2
            
            for friend in graph[race][individual]:
                if not segregated[race*n + friend]:
                    stash.append((friend, race, depth+1))
        return obscurity
"""You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist."""
