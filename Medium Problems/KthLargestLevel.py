# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        """
        :type root: Optional[TreeNode]    ANOTHER 100% PROBLEM OF THE DAY!
        :type k: int                        VERY HAPPY :)
        :rtype: int
        """
        #Each index of 'sums' corresponds to a layer in the binary tree
        sums=[]
        def getsum(self,ind):
            #append element instead of adding if the layer doesn't yet exist
            if len(sums)>ind:
                sums[ind]+=self.val
            else:
                sums.append(self.val)
            #start the function again if left or right exists
            if self.left:
                getsum(self.left,ind+1)
            if self.right:
                getsum(self.right,ind+1)
        #begin algorithm at index 0
        getsum(root,0)
        #check that k is in range
        if len (sums)<k:
            return -1
        #return kth largest sum.
        return sorted(sums)[-k]
