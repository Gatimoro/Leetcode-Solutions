
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        allval = []
        def move(node):
            if not node:
                return
            allval.append(node.val)
            move(node.right)
            move(node.left)
        move(root1)
        move(root2)
        return sorted(allval)
"""Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order."""
