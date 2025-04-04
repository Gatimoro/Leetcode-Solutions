# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def trav(node,lev):
            if not node:
                return node, lev
            r_node, r_depth = trav(node.right,lev + 1)
            l_node, l_depth = trav(node.left,lev + 1)
            if r_depth > l_depth:
                return r_node, r_depth
            elif r_depth < l_depth:
                return l_node, l_depth
            else:
                return node, r_depth
        return trav(root,0)[0]
      
"""Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A."""




#first attempt

# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         dep = 0
#         ans = 0
#         def trav(node,lev):
#             nonlocal dep
#             nonlocal ans
#             if not node:
#                 dep = max(dep, lev)
#                 return lev
#             r = trav(node.right,lev + 1)
#             l = trav(node.left,lev + 1)
#             if r == l == dep:
#                 dep = lev
#                 ans = node
            

#             return max(l,r)
#         trav(root,0)
#         return ans
