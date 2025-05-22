// You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

// Each queries[i] represents the following action on nums:

// Decrement the value at each index in the range [li, ri] in nums by at most 1.
// The amount by which the value is decremented can be chosen independently for each index.
// A Zero Array is an array with all its elements equal to 0.

// Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.
use std::{collections::BinaryHeap, cmp::Reverse};
impl Solution {
    pub fn max_removal(nums: Vec<i32>, mut queries: Vec<Vec<i32>>) -> i32 {
        queries.sort_unstable_by_key(|q| Reverse(q[0]));
        let mut hip = BinaryHeap::new();
        let mut curry = 0;
        let mut delta = vec![0; nums.len()];
        for i in 0..nums.len(){
            while let Some(q) = queries.last(){
                if q[0] > i as i32{
                    break;
                }
                hip.push(queries.pop().unwrap()[1]);
            }
            while curry < nums[i]{
                if let Some(end) = hip.pop(){
                    if end < i as i32{continue;}
                    curry += 1;
                    delta[end as usize] += 1;
                }else{
                    return -1;
                }
            }
            // println!("{}, {:?}", curry, queries);
            curry -= delta[i];

        }
        hip.len() as i32
    }
}
