# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.right or root.left:
            stacc=deque([(root.right,root.left)])
            while stacc:
                n1, n2 = stacc.pop()
                if not(n1 and n2) or n1.val != n2.val:
                    return False
                if n1.right or n2.left: stacc.append((n1.right,n2.left))
                if n1.left or n2.right: stacc.append((n1.left,n2.right))
        return True        
"""Check if binary tree is equal to itself's mirror"""
