// Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

// A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).
impl Solution {
    pub fn build_array(nums: Vec<i32>) -> Vec<i32> {
        let mut clone = vec![0;nums.len()];
        for (i, &n) in nums.iter().enumerate(){
            clone[i] = nums[n as usize];
        }
        clone
    }
}
