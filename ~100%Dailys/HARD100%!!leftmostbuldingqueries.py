class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        mtr=list(reversed(list(accumulate(reversed(heights[1:]),max))))+[0]#ARRAY with the Maximum number to the right (Max To Right --> mtr)
        stack=deque([])
        nbn=[-1]*len(heights)
        ans=deque([])
        for i , n in enumerate(heights):#create nbn (Next Bigger Number), it stores the index of the next number bigger than the current one
            while stack and stack[-1][1]<n:
                nbn[stack.pop()[0]]=i
            stack.append([i,n])
        for q in queries:
            if q[0]<=q[1]: #make a the lowest index and b the highest index
                a , b = q[0] , q[1]
            else:
                b , a = q[0] , q[1]
            
            if heights[b]>heights[a] or a==b: #in the case that a==b they are already on the same building so return b, the answer will also be b if the eight of a is smaller, as alice can just walt to bob's building.
                ans.append(b)
            elif nbn[a]==-1 or nbn[b]==-1: #if a or b are -1 and they are not on the same building, it means that for one of the heights, there isn't any building bigger than itself to the right
                ans.append(-1)
            elif nbn[a]<b: #if the next biggest building's index is less than b and the height at b is lower than a, we must find by hand(or computer in this case) an index greater than b whose height is greater than a
                if mtr[b]<heights[a]: #if the max number to the right of b is less than a (remember b<a), there is no index.
                    ans.append(-1)
                else:
                    b+=1
                    while heights[a]>=heights[b]: #now that we checked for the existance of an answer, we traverse the array until we find it.
                        b+=1
                    ans.append(b)
            else:
                ans.append(max(nbn[b],nbn[a]))
        return list(ans)
"""DESCRIPTION
2940. Find Building Where Alice and Bob Can Meet
Hard
You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1."""

 
