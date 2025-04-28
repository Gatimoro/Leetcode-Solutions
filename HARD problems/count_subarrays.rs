impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i64) -> i64 {
        let mut sum: i64 = 0;
        let mut length: i64 = 0;
        let mut count: i64 = 0;
        let mut cur: usize = 0;
        while cur < nums.len(){
            length += 1;
            sum += nums[cur] as i64;
            cur += 1;
            while length >= 1 && sum * length >= k{
                sum -= nums[cur - length as usize] as i64;
                length -= 1;
            } 
            count += length;
        }count
    }
}
// The score of an array is defined as the product of its sum and its length.

// For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
// Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

// A subarray is a contiguous sequence of elements within an array.

