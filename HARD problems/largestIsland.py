class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        group = 1 #the island number
        depth=[0,0] #size of each island, island numbers start from 2
        bounds=set()
        for x in range(len(grid)):
            for y in range(len(grid)):
                if grid[x][y] == 1: #we found land!
                    span=0          #size of island
                    group+=1        #island number
                    agar = deque([(x,y)])#an agar to store connected cells
                    while agar:
                        i, j = agar.popleft()
                        if not j!=-1!=i or not j!=len(grid)!=i or grid[i][j]>=2:#bound check
                            continue
                        if grid[i][j]==0: #if we came to a water cell from land, it must be a bound cell that we must check in the future
                            bounds.add((i,j))
                            continue
                        grid[i][j]=group #update each land cell to the island number
                        span+=1          #increase size
                        for neighbor in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)): agar.append(neighbor) #add each neighbor to the queue
                    depth.append(span) #add the final size of the island to depth[island number]
        if len(depth)==2: return 1 #check that there was at least 1 island found
        if bounds:
            ans=0
            for x,y in bounds:
                touches=set()                               #keep track of which islands are connected to the water cell
                if x!=-1+len(grid):touches.add(grid[x+1][y])#check bounds and add the group to the set.
                if x!=0:touches.add(grid[x-1][y])
                if y!=-1+len(grid):touches.add(grid[x][y+1])
                if y!=0:touches.add(grid[x][y-1])
                cur=0
                for g in touches: cur+=depth[g]             #add depth of each island that touches the cell to 
                if cur>ans: ans = cur #update ans if the current size exceeds it.
            return ans+1
        else: return depth[2] #if no bounds, it means that there is just 1 big island   
  """You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s."""
