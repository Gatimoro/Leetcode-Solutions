use std::collections::HashMap;
impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        let (mut left, mut total_subarrays, mut count) = (0, 0, 0);
        let mut appearences = HashMap::new();
        for num in nums.iter(){
            *appearences.entry(num).or_insert(-1) += 1;
            count += appearences.get(num).unwrap();
            while count >= k{
                count -= appearences.get(&nums[left]).unwrap();
                *appearences.get_mut(&nums[left]).unwrap() -= 1;
                left += 1;
            }
            total_subarrays += left as i64;
        }total_subarrays
    }
}
// Given an integer array nums and an integer k, return the number of good subarrays of nums.

// A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

// A subarray is a contiguous non-empty sequence of elements within an array.

