class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        target = len(graph)
        if target==1:return 0 #testcase. smh
        bong = deque([(n, 1<<n, 0) for n in range(target)]) #the stack, with each node initialized to start the bfs from each node.
        states=[[False for _ in range(1<<target)] for _ in range(target)] #keep track of node + seen combinations. states[node][seen] == True means that that node has already been visited with the same seen nodes before. 
        goal = (1<<target)-1 #if seen == 111...1, it means that every node has been visited. We have 'target' nodes so we need 'target' 1s
        
        while True:
            cur, seen, depth = bong.popleft()
            for n in graph[cur]:
                new = seen | (1<<n) #add the next node to seen
                if new == goal: return depth + 1 #check if target reached
                if not states[n][new]: #check for redundancy
                    states[n][new] = True 
                    bong.append((n,new,depth+1))
"""You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges."""
