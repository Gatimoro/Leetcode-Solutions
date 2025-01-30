# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumbo = ListNode(next=head)
        dumbus= ListNode(next=head)
        while head:
            dumbus=dumbus.next
            while dumbus.next and dumbus.next.val==head.val:
                dumbus=dumbus.next
            head.next=dumbus.next
            head=head.next
        return dumbo.next
"""remove duplicates from linked list""
