// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
//DESCRIPTION: CHECK IF THE TREE IS BALANCED.
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        fn inv(node: Option<Rc<RefCell<TreeNode>>>, depth: i32) -> (bool, i32){
            if let Some(node) = node{
                let node = node.borrow();
                let (lt,ld) = inv(node.left.clone(), depth + 1);
                let (rt,rd) = inv(node.right.clone(), depth + 1);
                return (rt && lt && ld.abs_diff(rd) <= 1, ld.max(rd));
            }       
            (true, depth)
        }
        return inv(root,0).0
    }
}
