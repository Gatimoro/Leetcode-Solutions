impl Solution {
    pub fn add_two_numbers(mut l1: Option<Box<ListNode>>, mut l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut carry = 0;
        let mut reti = ListNode::new(0);
        let mut cur  = &mut reti;
        
        
        while !l1.is_none() || !l2.is_none() || carry == 1{
            if let Some(n1) = l1{
                carry += n1.val;
                l1 = n1.next;
            }
            if let Some(n2) = l2{
                carry += n2.val;
                l2 = n2.next;
            }
            cur.next = Some(Box::new(ListNode::new(carry%10)));
            cur = cur.next.as_mut().unwrap();
            carry /= 10;
        }
        reti.next
    }
}
// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
