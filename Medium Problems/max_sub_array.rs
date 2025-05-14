//return the sum of the elements of the subarray with the maximum sum.
impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let (mut cur, mut max) = (0, i32::MIN);
        for n in nums{
            cur += n;
            max = max.max(cur);
            if cur < 0{
                cur = 0;
            }
        }
        max
    }
}
