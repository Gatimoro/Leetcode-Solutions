impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        let (mut a,mut b) = (i32::MAX, i32::MAX);
        for &num in nums.iter(){
            if num <= a{
                a = num;
            }else if num <= b{
                b = num;
            }else{
                return true;
            }
        }
        false
    }
}
//Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
