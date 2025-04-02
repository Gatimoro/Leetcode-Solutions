impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut ans = 0 as i64;
        for i in 0..n{
            for j in i+1..n{
                for k in j+1..n{
                    ans = ans.max((nums[i] as i64 -nums[j] as i64) * nums[k] as i64)
                }
            }
        }
        ans
    }
}
//You are given a 0-indexed integer array nums.

//Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

//The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
