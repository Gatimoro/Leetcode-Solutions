use std::collections::HashSet;
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let dif: HashSet<i32> = nums.into_iter().collect();
        if let Some(thing) = dif.iter().min(){
            if thing<&k{return -1;}
            if thing == &k{return (dif.len()-1) as i32}
        }
        dif.len() as i32
    }
}
// You are given an integer array nums and an integer k.

// An integer h is called valid if all values in the array that are strictly greater than h are identical.

// For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

// You are allowed to perform the following operation on nums:

// Select an integer h that is valid for the current values in nums.
// For each index i where nums[i] > h, set nums[i] to h.
// Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.
