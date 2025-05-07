impl Solution {
    pub fn three_sum_closest(mut nums: Vec<i32>, target: i32) -> i32 {
        nums.sort();
        let n = nums.len();
        let mut best = i32::MAX;
        let mut closest = -1;
        for (i, num) in nums.iter().enumerate(){
            let (mut left, mut right) = ( i+1, n-1);
            let goal = target - num;
            
            while left < right{
                let closeness = goal - nums[ left ] - nums[ right ];
                // println!("{},{},{}",num, nums[left], nums[right]);

                if closeness.abs() < best{ 
                    best = closeness.abs(); 
                    closest = num + nums[left] + nums[right];
                }
                if closeness > 0{
                    left += 1;
                }else if closeness < 0{
                    right -= 1;
                }else{
                    return target;
                }
                // println!("{}", closest);
            }
        }
        closest 
    }
}
// Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

// Return the sum of the three integers.

// You may assume that each input would have exactly one solution.
