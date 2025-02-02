# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=list()
        prev=None
        while head:
            nex = head.next
            head.next= prev
            prev=head
            head=nex
        return prev
"""reverse nodes in list"""
