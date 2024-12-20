# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        odd=True
        nodes=deque([[root]])
        while nodes[-1][-1].left:
            nodes.append([])
            for node in nodes[-2]:
                nodes[-1].append(node.left)
                nodes[-1].append(node.right)
            if odd:
                for start in range(2**(len(nodes)-2)):
                    hold=nodes[-1][start].val
                    nodes[-1][start].val = nodes[-1][-start-1].val
                    nodes[-1][-start-1].val=hold
            odd = not odd
        return root
"""Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node."""
