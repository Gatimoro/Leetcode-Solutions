# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]      HOLY CRAP THIS IS EVEN WORSE
        :rtype: List[int]                     
        """
        ans=[]
        vals=[]
        ind=0
        self=head
        while self:
            vals.append(self.val)
            self=self.next
        for x in vals:
            happy=False
            for y in vals[ind:]:
                if y>x:
                    happy=True
                    ans+= [y]
                    break
            if not happy:
                ans+= [0]
            ind+=1
        return ans
