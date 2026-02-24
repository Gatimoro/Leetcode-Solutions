# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], cur = 0) -> int:
        cur <<= 1 
        cur |= root.val
        if not (root.left or root.right):
            return cur
        return (self.sumRootToLeaf(root.left, cur) if root.left else 0) + (self.sumRootToLeaf(root.right, cur) if root.right else 0)
