impl Solution {
    pub fn subset_xor_sum(nums: Vec<i32>) -> i32 {
        fn compute(cur: i32, index: usize, nums: &Vec<i32>) -> i32 {
            let result = if index == nums.len() {cur} else {compute(cur ^ nums[index], index + 1, &nums) + compute(cur, index + 1, &nums)};
            return result;
        }
        return compute(0, 0, &nums)
    }
}
//The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

//For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
//Given an array nums, return the sum of all XOR totals for every subset of nums. 

//Note: Subsets with the same elements should be counted multiple times.

//An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

 

