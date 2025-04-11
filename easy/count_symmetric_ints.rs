impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut ans = 0;
        for cand in 11.max(low)..=(100.min(high)){
            if cand % 10 == cand / 10{
                ans += 1;
            }
        }
        for cand in 1000.max(low)..=high{
            if cand % 10 + cand %100 /10 == cand%1000 /100 + cand/1000{
                ans += 1;
            } 
        }ans
    }
}
// You are given two positive integers low and high.

// An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

// Return the number of symmetric integers in the range [low, high].
