class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans=[]
        pths=[i for i in range(n)]
        saltos=[[] for i in range(n)]#saltos means jumps in spanish
        #Starting at current city(cur), skip until you find a jump and return if you are over the shortest path to that city
        def find(cur,leng):
            nonlocal pths
            while cur<n-1 and not saltos[cur]:
                if leng>=pths[cur]:
                    return
                else:
                    pths[cur]=leng
                cur+=1
                leng+=1
            if leng>=pths[cur]:
                return
            else:
                pths[cur]=leng
                if n-1==cur:
                    return
            #check all the jumps for a shorter path and follow through with it if found.
            for jump in saltos[cur]:
                find(jump,leng+1)
            find(cur+1,leng+1)
        """since each time we add a new shortcut we either get a shorter or the same path length, 
        we will make sure the new shortcut is used by starting find() after making the jump. 
        After the jump find() will start at city shortcut[1], with the length to reach it 
        being the shortest path to shortcut[0]+1."""
        for x in queries:
            saltos[x[0]].append(x[1])
            find(x[1],pths[x[0]]+1)
            ans.append(pths[-1])
        return ans
            
