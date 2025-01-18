# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque([(root,0)])
        ans=[]
        curlen=-1
        while nodes:
            node,level=nodes.popleft()
            if node:
                if level>curlen:
                    ans.append([])
                    curlen+=1
                ans[level].append(node.val)
                nodes.append((node.left,level+1))
                nodes.append((node.right,level+1))
        return ans

