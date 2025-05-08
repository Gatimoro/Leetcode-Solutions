//asess whether 2 binary trees have leafs with the same values and order.
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn leaf_similar(root1: Option<Rc<RefCell<TreeNode>>>, root2: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let (mut left, mut right) = (Vec::new(), Vec::new());
        fn trav(rc_option: Option<Rc<RefCell<TreeNode>>>, vector: &mut Vec<i32>){
            if let Some(rc_node) = rc_option{
                let ref_node = rc_node.borrow();
                let (l, r) = (ref_node.left.clone(), ref_node.right.clone());
                if l.is_none() && r.is_none(){
                    vector.push(ref_node.val);
                }else{
                    trav(l, vector);
                    trav(r, vector);
                }
            }
        }
        trav(root1, &mut left);
        trav(root2, &mut right);
        left == right
    }
}
