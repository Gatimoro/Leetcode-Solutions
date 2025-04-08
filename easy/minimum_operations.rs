use std::collections::HashSet;
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        for (i, elem) in nums.into_iter().enumerate().rev(){
            if seen.contains(&elem){return ((i  as i32)/ 3) + 1;}
            seen.insert(elem);
        }0
    }
}

// You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

// Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
// Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
