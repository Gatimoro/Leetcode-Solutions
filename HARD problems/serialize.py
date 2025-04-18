"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself."""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        """
        if not root:return ''
        ret = []
    
        def move(node):
            ret.append(str(node.val))
            if node.left:
                ret.append('l')
                move(node.left)
            if node.right:
                ret.append('r')
                move(node.right)
            ret.append('n')
        move(root)
        print(ret)
        return '$'.join(ret)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        """
        nodes = data.split('$')
        if not data:
            return None

        root = TreeNode(int(nodes[0]))
        def build(node,i):
            if nodes[i]=='n':
                return i+1
            if nodes[i] == 'l':
                node.left = TreeNode(int(nodes[i+1]))
                i=build(node.left, i+2)
            if nodes[i]=='n':
                return i+1
            if nodes[i] == 'r':
                node.right = TreeNode(int(nodes[i+1]))
                i=build(node.right, i+2)
            if nodes[i]=='n':
                return i+1
            return i
        build(root,1)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


