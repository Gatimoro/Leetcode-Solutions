impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut dif = 0 as i64;
        let mut max_seen= nums[0] as i64;
        let mut ans = 0 as i64;
        let mut num;
        for n in nums{
            num = n as i64;
            ans = ans.max(dif * num);
            dif = dif.max(max_seen - num);
            max_seen = max_seen.max(num as i64);
        }
        ans
        
        
    }
}
