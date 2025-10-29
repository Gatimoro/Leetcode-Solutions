// You are given a positive number n.

// Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits
impl Solution {
    pub fn smallest_number(n: i32) -> i32 {
        return (2 << n.ilog(2)) - 1
    }
}
