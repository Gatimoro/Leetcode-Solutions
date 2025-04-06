// Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

// answer[i] % answer[j] == 0, or
// answer[j] % answer[i] == 0
// If there are multiple solutions, return any of them.

impl Solution {
    pub fn largest_divisible_subset(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort();
        let mut ret = vec![];
        let mut longest = vec![vec![]; nums.len()];
        for i in (0..nums.len()){
            longest[i] = vec![nums[i]];
        }
        for i in (0..nums.len()).rev(){
            let mut j = i + 1;
            while j < nums.len(){
                if  nums[j] % nums[i] == 0 && longest[j].len() +1 > longest[i].len(){
                    longest[i] = longest[j].clone();
                    longest[i].push(nums[i]);
                }
                j+=1;
            }
            if longest[i].len() > ret.len(){ret = longest[i].clone()};
        }
        ret
    }
}
