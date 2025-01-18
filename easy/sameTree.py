# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:   
        return True if not (p or q) else False if not (p and q) else self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) if p.val==q.val else False
