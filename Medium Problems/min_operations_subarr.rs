// You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.

// In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.

// Return the minimum number of operations required to make all elements in the array 0.
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut stacc = vec![];
        let mut total = 0;
        for n in nums {
            if n == 0 {
                stacc.clear();
            } else {
                while !stacc.is_empty() && *stacc.last().unwrap() > n {
                    stacc.pop();
                }
                if stacc.is_empty() || *stacc.last().unwrap() != n {
                    total += 1;
                    stacc.push(n);
                }
            }
        }
        total
    }
}
