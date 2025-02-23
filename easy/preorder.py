# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, start: Optional[TreeNode]) -> List[int]:
        stash = deque([start])
        ans=[]
        while stash:
            root = stash.pop()
            if root:
                ans.append(root.val)
                stash.append(root.right)
                stash.append(root.left)
        return ans
