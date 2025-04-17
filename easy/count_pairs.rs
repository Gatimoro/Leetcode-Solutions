impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        let mut count = 0;
        for i in 0..nums.len(){
            for j in i+1..nums.len(){
                if ( ((j*i) as i32)%k == 0) && (nums[i] == nums[j]){
                    count += 1;
                }
            }
        }count
    }
}
// Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
