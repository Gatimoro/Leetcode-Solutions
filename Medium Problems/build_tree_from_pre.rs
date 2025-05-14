//build a tree from the preorder and inorder traversals.
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn add_nodes(pre: &[i32], eno: &[i32] ) -> Option<Rc<RefCell<TreeNode>>>{
            if eno.is_empty(){
                return None;
            }
            let root = pre[0];
            let idx = eno.iter().position(|&x| x == root).unwrap();
            let mut node = Rc::new(RefCell::new(TreeNode::new(root)));
            node.borrow_mut().left = add_nodes(&pre[1..=idx] ,&eno[..idx]);
            node.borrow_mut().right = add_nodes(&pre[idx + 1..], &eno[idx + 1..]);
            Some(node)
        }
        add_nodes(&preorder, &inorder)
    }
}

