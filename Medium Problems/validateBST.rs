// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn check(node: Option<Rc<RefCell<TreeNode>>>, max_allowed: i64, min_allowed: i64) -> bool{
            if let Some(node) = node{
                let node = node.borrow();
                let v = node.val as i64;
                if v <= min_allowed || v >= max_allowed{
                    return false;
                };
                let left = node.left.clone();
                let right = node.right.clone();
                check(right, max_allowed,min_allowed.max(v)) && check(left, max_allowed.min(v), min_allowed) 
            }else{
                true
            }
        }
        check(root, i64::MAX, i64::MIN)
    }
}
