
impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0;arr.len() + 1];
        for i in 1..=arr.len(){
            let mut max_in_window = 0;
            for shift in 1..=k.min(i){
                max_in_window = max_in_window.max(arr[i-shift]);
                dp[i] = dp[i].max(max_in_window * shift as i32 + dp[i-shift]);
            }
        }
        dp[arr.len()]
    }
}
// Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

// Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.
