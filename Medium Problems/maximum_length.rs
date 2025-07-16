//You are given an integer array nums.
// A subsequence sub of nums with length x is called valid if it satisfies:

// (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
// Return the length of the longest valid subsequence of nums.

// A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        // first num _ second num.    from the longest subseq
        let (mut even_even, mut even_odd, mut odd_even, mut odd_odd) = (0, 0, 0, 0);
        for n in nums{
            let is_even = n % 2 == 0;
            if is_even{
                even_even += 1;
                if odd_even % 2 == 1{
                    odd_even += 1;    
                }
                if even_odd % 2 == 0{
                    even_odd += 1;    
                }
            }else{
                odd_odd += 1;
                if odd_even % 2 == 0{
                    odd_even += 1;    
                }
                if even_odd % 2 == 1{
                    even_odd += 1;    
                }
            }
        }
        even_even.max(even_odd).max(odd_even).max(odd_odd)
    }
}
