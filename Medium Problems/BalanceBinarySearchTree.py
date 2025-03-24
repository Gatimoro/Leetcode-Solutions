class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ordered = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            ordered.append(node.val)
            inorder(node.right)
        inorder(root)
        def create(l,r):
            if l>r:
                return None
            middle = (l + r) >> 1
            turner = TreeNode(ordered[middle])
            turner.right = create(middle+1, r)
            turner.left = create(l, middle-1)
            return turner
        return create(0, len(ordered)-1)
"""Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1."""
