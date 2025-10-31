# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = set()
        used = set()
        ans = []
        def travv(node):
            nonlocal ans
            nonlocal seen
            if not node:
                return ''

            reti = str(node.val) +' ' + travv(node.left)+' ' + travv(node.right)
            
            if reti in seen and reti not in used:
                ans.append(node)
                used.add(reti)
            seen.add(reti)
            return reti
        travv(root)
        return ans
