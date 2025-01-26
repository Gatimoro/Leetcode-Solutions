class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        need=[0]*numCourses
        unblock = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            unblock[p].append(c)
            need[c]+=1
        stack=deque([course for course in range(numCourses) if need[course]==0])
        while stack:
            cur = stack.pop()
            for link in unblock[cur]:
                need[link]-=1
                if need[link]==0:
                    stack.append(link)
        return not any(need)
"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false."""
