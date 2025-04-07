impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {
        let mut target:i32 = nums.iter().sum();
        if target % 2 == 1{
            return false;
        }target >>= 1; 
        let mut dp = vec![false; (target + 1) as usize];
        dp[0] = true;
        for num in nums.into_iter(){
            for i in (num..=target).rev(){
                dp[i as usize] |= dp[(i-num) as usize];
            }
        }dp[target as usize]
    }
}
// Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
