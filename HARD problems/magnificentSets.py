


class Solution:"""I am super glad of this solution. I didn't solve it immediately but I learned a great amount of stuff along the way"""
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        joints = [[] for _ in range(n+1)]#adjacency array
        for a, b in edges:
            joints[a].append(b)
            joints[b].append(a)
        color = [None] * (n+1) #array to check if node visited
        weedSelection=[]#this will store the nodes for each connected component in the graph.

        for joint in range(1,len(joints)): #Check each connected component for bipartiteness, for else we can't assign groups to it. (and we return -1)
            if color[joint]==None:
                weedSelection.append([joint])#each time we see a new component, ie an unvisited node, add a new layer to our connected component container weedSelect
                color[joint] = True
                toCheck = deque([joint])
                while toCheck:
                    node = toCheck.pop()
                    shade = color[node]
                    for neighbor in joints[node]:
                        if color[neighbor]==None:
                            color[neighbor] = not shade
                            toCheck.append(neighbor)
                            weedSelection[-1].append(neighbor)#add each node to the connected component container
                        elif color[neighbor]==shade:
                            return -1
        elevation=0  #how high we be gettin'
        for strain in weedSelection: #we choose a strain
            high,stash = 1,1 #set the initial stash and high (cur depth +1 and max depth+1)
            for bud in strain: #now we take each bud (node) from the strain (connected component)
                blunt_rotation=[0]*(1+n) #reset the visited check
                blunt_rotation[bud]=True
                bongStack = deque([(bud,1)])
                while bongStack: #run the usual bfs depth check starting from 1
                    bud, stash = bongStack.popleft()
                    for joint in joints[bud]:
                        if not blunt_rotation[joint]:
                            blunt_rotation[joint]=True
                            bongStack.append((joint,stash+1))
                high=max(high,stash) #store the maximum depth we found in the component
            elevation+=high #and add it to the answer.
        return elevation


