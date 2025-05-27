//find differenc of the sums of integens less than n that are and are not divisible by m
impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        n * (n + 1) / 2 - (n / m) * (n / m + 1) * m
    }
}
