# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        stack=deque([[root,0]])
        bylev=deque([[]for _ in range(1000)])
        ans = 0
        while stack:
            nod,lev=stack.pop()
            if nod:
                if lev+1==len(bylev):
                    bylev.append([])
                stack.append([nod.right,lev+1])
                stack.append([nod.left,lev+1])
                bylev[lev].append(nod.val)

        sort=[sorted(l) for l in bylev]
        x=0
        while bylev[x]:
            for y in range(len(bylev[x])):
                while bylev[x][y]!=sort[x][y]:
                    ind=sort[x].index(bylev[x][y])
                    bylev[x][y],bylev[x][ind]=bylev[x][ind],bylev[x][y]
                    ans+=1
            x+=1
        return ans
"""Desscription:
2471. Minimum Number of Operations to Sort a Binary Tree by Level
Medium
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node."""  
