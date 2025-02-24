class Solution: """very interesting and cool to write and optimize problem"""
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        #amount of nodes
        node_amount=len(amount)

        #build graph
        connects = [[] for _ in range(node_amount)]
        
        for a, b in edges:
            connects[a].append(b)
            connects[b].append(a)

        #get the path bob traverses and store when he reaches each node.
        whenBobReaches = [float('inf') for _ in range(node_amount)]
        def bobfinds(parent, current, depth):
            if current == 0: 
                return True #:}>=<
            for n in connects[current]:
                if n != parent:
                    if bobfinds(current, n, depth+1):
                        whenBobReaches[current] = depth
                        return True
            return False
        bobfinds(-1,bob,0)
        whenBobReaches[bob]=0

        #time to compute every path to a leaf that alice may take
        profit = float('-inf')
        alice_pos = deque([(0,0,0,0)]) #this is the parent node, current node, the current profit and the moves it took to get here.
        while alice_pos:
            last, curr, moneys, moves = alice_pos.pop()
            #if we arrive faster than bob, we are the ones to open the gate
            if moves < whenBobReaches[curr]:
                moneys+=amount[curr]
            #but if we arrive at the same time, we split the profit
            elif moves == whenBobReaches[curr]:
                moneys+=amount[curr]//2
            #then check neightbors
            for n in connects[curr]:
                if n != last:
                    #if neighbor is leaf
                    if len(connects[n])==1:
                        #case where bob is a leaf
                        if n==bob:
                            candidate = moneys
                        #any other leaf will not be visited by bob, because he goes straight towards node 0
                        else:
                            candidate = moneys+amount[n]
                        #update profit
                        if candidate>profit:
                            profit = candidate
                    #if it ain't continue searching
                    else:
                        alice_pos.append((curr, n, moneys, moves+1))
        return profit
"""There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node."""
