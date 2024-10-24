# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val   
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def backotracko(root1,root2):
            #first check if both values are missing or we've reached an endpoint
            if not root1 and not root2:
                return True
            #if only one is missing, that's a discrepancy and return false
            elif not root1 or not root2:
                return False
            #now check if val1=val2 and repeat the process for the flipped and nonflipped next nodes.
            return root1.val==root2.val and (backotracko(root1.left,root2.right)and backotracko(root1.right,root2.left) or backotracko(root1.left,root2.left)and backotracko(root1.right,root2.right))
        return backotracko(root1,root2)
