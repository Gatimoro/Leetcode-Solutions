# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        return_dummy=ListNode(next=dummy)
        c=0
        while head:
            head=head.next
            c+=1
        for _ in range(c-n):
            dummy=dummy.next
        dummy.next=dummy.next.next
        return return_dummy.next.next
"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""
