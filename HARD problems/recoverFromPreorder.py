# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        bananatree = []
        i=0
        while i<len(traversal):
            curr = 0
            while traversal[i] == '-':
                curr+=1
                i+=1
            start_num = i
            while i<len(traversal) and traversal[i] != '-':
                i+=1
            bananatree.append((curr,int(traversal[start_num:i])))
        print(bananatree)
        i=1
        root = TreeNode(val = bananatree[0][1])
        def move(start, depth):
            nonlocal i
            #current depth must be 'depth'
            if i < len(bananatree) and depth == bananatree[i][0]:
                start.left = TreeNode(val=bananatree[i][1])
                i+=1
                move(start.left, depth + 1)
            if i < len(bananatree) and depth == bananatree[i][0]:
                start.right = TreeNode(val=bananatree[i][1])
                i+=1
                move(start.right, depth + 1)
        move(root,1)
        return root
