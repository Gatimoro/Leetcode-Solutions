use std::collections::HashMap;
impl Solution {
    pub fn count_interesting_subarrays(nums: Vec<i32>, modulo: i32, k: i32) -> i64 {
        let mut compl: HashMap<i32, i32>= HashMap::new(); // this will store the amount of times we've seen [index]
        *compl.entry(0).or_insert(0)+= 1;
        let mut curr = 0; //how many nums % modulo == k we've seen.
        let mut ans = 0;
        for num in nums{
            let valid = num % modulo == k;
            curr = (curr + valid as i32) % modulo;
            ans += *compl.get(&((curr - k + modulo) % modulo)).unwrap_or(&0) as i64;
            // k === curr - compl MOD modulo
            // curr - k + moduulo === compl MOD modulo
            *compl.entry(curr).or_insert(0)+= 1;
        }ans
    }
}
// You are given a 0-indexed integer array nums, an integer modulo, and an integer k.

// Your task is to find the count of subarrays that are interesting.

// A subarray nums[l..r] is interesting if the following condition holds:

// Let cnt be the number of indices i in the range [l, r] such that nums[i] % modulo == k. Then, cnt % modulo == k.
// Return an integer denoting the count of interesting subarrays.

// Note: A subarray is a contiguous non-empty sequence of elements within an array.

