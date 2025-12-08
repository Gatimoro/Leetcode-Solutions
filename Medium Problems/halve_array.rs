// You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)

// Return the minimum number of operations to reduce the sum of nums by at least half.
use std::collections::BinaryHeap;
impl Solution {
    pub fn halve_array(nums: Vec<i32>) -> i32 {
        let mut hip = BinaryHeap::new();
        let mut total: i64 = 0;
        for &n in &nums {
            let scaled = (n as i64) << 20; 
            hip.push(scaled);
            total += scaled >> 1;
        }
        let mut removed = 0;
        while total > 0{
            let c = hip.pop().unwrap() >> 1;
            hip.push(c);
            removed += 1;
            total -= c;
        }
        removed
    }
}
