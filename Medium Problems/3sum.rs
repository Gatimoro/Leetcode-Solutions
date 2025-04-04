impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        let mut sum = 0;
        let mut last_num = i32::MAX;

        for start in 0..nums.len(){
            if nums[start] == last_num{
                continue;
            }last_num = nums[start];
            
            let (mut left, mut right) = (start + 1,nums.len() - 1);
            while (left < right){
                sum = nums[start] + nums[left] + nums[right];
                if sum <= 0{
                    if sum == 0{
                        ans.push(vec![nums[start], nums[left], nums[right]]);
                    }
                    let bef = nums[left];
                    while nums[left] == bef && left < right{
                        left += 1;
                    }
                }else{ 
                    let bef = nums[right];
                    right -= 1;
                    while nums[right] == bef && left < right{
                        right -= 1;
                    }
                }
            }
        }
        return ans
    
    }
}
//Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

//Notice that the solution set must not contain duplicate triplets.
