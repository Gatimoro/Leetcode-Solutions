# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q=deque([root]) if root else 0
        largest=[]
        while q:
            top=-2147483648
            for _ in range(len(q)):
                val=q.popleft()
                top=max(top,val.val)
                if val.right:
                    q.append(val.right)
                if val.left:
                    q.append(val.left)
            largest.append(top)
        return largest
"""Description:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed)."""
