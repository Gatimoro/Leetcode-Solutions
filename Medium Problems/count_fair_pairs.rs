impl Solution {
    pub fn count_fair_pairs(mut nums: Vec<i32>, lower: i32, upper: i32) -> i64 {
        nums.sort();
        let (mut bot, mut top) = (0, nums.len());
        //I'll find the first number that is invalid. (first greater than)
        fn find(arr: &Vec<i32>, target: i32, mut l: usize, mut r: usize) -> usize{
            while l<r{
                let m = (l+r) / 2;
                if arr[m] <= target{
                    l = m + 1;
                    continue;
                }r = m;
            }r
        }
        let mut count = 0;
        //condition: lower <= sum <= upper
        for (i, &n) in nums.iter().enumerate(){
            let max_allowed = upper - n;
            top = find(&nums, max_allowed, i, top);
            
            bot = find(&nums, lower - n - 1, i+1, top);
            if bot > top{break;}
            count += (top - bot) as i64;
            
            // println!("{:?}", nums);
            // println!("top {}, bot {}, n {}", top,bot, n);
        }count

    }
}
// Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

// A pair (i, j) is fair if:

// 0 <= i < j < n, and
// lower <= nums[i] + nums[j] <= upper
