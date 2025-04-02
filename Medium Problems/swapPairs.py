class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = ListNode(next = head)
        turner_the_returner = node
        while node.next and node.next.next:
            a = node.next
            b = a.next
            c = b.next

            node.next = b
            b.next = a
            a.next = c
            node = a

        return turner_the_returner.next
"""Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)
 """
