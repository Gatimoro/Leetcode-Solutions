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
"""We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root."""
