# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        create=ListNode()
        root=ListNode(0,create)
        while list1 or list2:
            if not list2 or list1 and list2 and list1.val<list2.val:
                create.next=list1
                list1=list1.next
            else:
                create.next=list2
                list2=list2.next
            create=create.next
        return root.next.next
"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 """
