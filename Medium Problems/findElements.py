# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        gyatt = deque([(root,0)])
        self.seen = set()
        while gyatt:
            curr_node, val = gyatt.popleft()
            curr_node.val = val
            self.seen.add(val)
            if curr_node.right: gyatt.append((curr_node.right, 2*val + 2))
            if curr_node.left: gyatt.append((curr_node.left, 2*val + 1))

    def find(self, target: int) -> bool:
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
