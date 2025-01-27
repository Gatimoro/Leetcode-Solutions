class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        takeafter = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for first, second in prerequisites:
            takeafter[first].append(second)
            indegree[second] += 1
        topo_order = []
        queue = deque(i for i in range(numCourses) if indegree[i] == 0) 

        while queue:
            course = queue.popleft()
            topo_order.append(course)
            for neighbor in takeafter[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        preqs = [set() for _ in range(numCourses)]
        for course in topo_order:
            for neighbor in takeafter[course]:
                preqs[neighbor].update(preqs[course])  
                preqs[neighbor].add(course)  

        ans = []
        for query in queries:
            ans.append(query[0] in preqs[query[1]])
        return ans
"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query."""
