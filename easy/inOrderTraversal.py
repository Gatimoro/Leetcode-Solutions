# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def walk(root):
            nonlocal ans
            if root:
                walk(root.left)
                ans.append(root.val)
                walk(root.right)
        walk(root)
        return ans
            
