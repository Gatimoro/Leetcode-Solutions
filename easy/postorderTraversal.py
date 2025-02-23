# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root,False)])
        ans=[]
        while q:
            cur, seen = q.pop()
            if cur:
                if seen:
                    ans.append(cur.val)
                else:
                    q.append((cur,True))
                    if cur.right:q.append((cur.right,False))
                    if cur.left:q.append((cur.left,False))
        return ans
                    
