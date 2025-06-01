// You are given two positive integers n and limit.

// Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.
impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        let mut ans: i64 = 0;
        for i in 0..=limit.min(n) {
            if n - i > 2 * limit {
                continue;
            }
            ans += (n - i).min(limit) as i64 - 0.max(n - i - limit) as i64 + 1;
        }

        return ans;
    }
}
