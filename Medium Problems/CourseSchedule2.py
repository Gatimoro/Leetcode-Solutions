class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = [0] * numCourses
        unlock = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            preq[a]+=1
            unlock[b].append(a)
        q = deque()
        for c in range(numCourses):
            if not preq[c]:
                q.append(c)
        ans=list(q)
        while q:
            cur = q.popleft()
            for n in unlock[cur]:
                preq[n]-=1
                if not preq[n]:
                    q.append(n)
                    ans.append(n)
               
                    
        return ans if len(ans) == numCourses else []
"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array."""
