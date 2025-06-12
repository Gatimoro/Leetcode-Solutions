impl Solution {
    pub fn max_adjacent_distance(nums: Vec<i32>) -> i32 {
        let mut ret = 0;
        for i in 0..nums.len()-1{
            ret = ret.max((nums[i] - nums[i + 1] ).abs());
        }
        ret.max((nums[0] - nums[nums.len() - 1]).abs())
    }
}
