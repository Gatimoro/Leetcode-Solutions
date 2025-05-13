use std::collections::VecDeque;
impl Solution {
    pub fn length_after_transformations(s: String, t: i32) -> i32 {
        let mut letts = [0; 26];
        let MOD = 1_000_000_007;
        for c in s.chars(){
            letts[c as usize - 'a' as usize] += 1;
        }
        let mut dekk = VecDeque::from(letts);
        for _ in 0..t{
            let a = dekk.pop_back().unwrap_or(0);
            let b = dekk.pop_front().unwrap_or(0);
            dekk.push_front((a + b) % MOD);
            dekk.push_front(a);
        }
        (dekk.into_iter().map(|x| x as i64).sum::<i64>() % MOD as i64) as i32
    }
}
// You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

// If the character is 'z', replace it with the string "ab".
// Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
// Return the length of the resulting string after exactly t transformations.

// Since the answer may be very large, return it modulo 109 + 7.

 
