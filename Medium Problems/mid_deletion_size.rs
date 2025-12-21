// You are given an array of n strings strs, all of the same length.

// We may choose any deletion indices, and we delete all the characters in those indices for each string.

// For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

// Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.
impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let m = strs.len();
        let n = strs.first().map_or(0, |s| s.len());
        
        let mut inorder = 0_u128; 
        let mut count   = 0;

        for col in 0..n {
            let mut new_inorder = 0_u128;

            for row in 1..m {
                if inorder & 1 << row != 0 { 
                    continue; 
                }
                let prev = strs[row - 1].as_bytes();
                let curr = strs[row    ].as_bytes();

                if prev[col] < curr[col] {
                    new_inorder |= 1 << row;
                } else if prev[col] > curr[col] {
                    count += 1;
                    new_inorder = 0;
                    break;
                } 
            }
            inorder |= new_inorder;
        }
        count
    }
}
