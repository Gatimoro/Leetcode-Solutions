// In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

// As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.
impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut seen = vec![false; 103];
        let mut out = vec![]; 
        for n in nums{
            if seen[n as usize]{
                out.push(n);
            }
            seen[n as usize] = true;
        }
        out
    }
}
