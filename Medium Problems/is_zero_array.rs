//You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

// For each queries[i]:

// Select a subset of indices within the range [li, ri] in nums.
// Decrement the values at the selected indices by 1.
// A Zero Array is an array where all elements are equal to 0.

// Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.


impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        let mut cumu = vec![0;nums.len() + 1];
        for x in queries{
            let l = x[0];
            let r = x[1] + 1;
            cumu[l as usize] += 1;
            cumu[r as usize] -= 1
        }
        let mut sum = 0;
        for (num, cum) in nums.into_iter().zip(cumu){
            sum += cum;
            if sum < num{
                return false
            }
        }
        return true
    }
}
