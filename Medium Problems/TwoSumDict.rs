use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let n = nums.len();
        let mut pairs = HashMap::new();
        for (i, num) in nums.iter().enumerate(){
            if pairs.contains_key(num){
                return vec![i as i32, pairs[num]];
            }pairs.insert(target-num, i as i32);
        }vec![]

    }
}
"""Find the indices of any two numbers that add up to target."""
