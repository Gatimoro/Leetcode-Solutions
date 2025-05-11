// You are given a string s consisting of lowercase English letters, and an integer k.

// Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters in the resulting string is at most k.

// Return the minimum number of deletions required to achieve this.©leetcode
use std::collections::HashMap;
impl Solution {
    pub fn min_deletion(s: String, k: i32) -> i32 {
        let mut seen = HashMap::new();
        for c in s.chars() {
            *seen.entry(c).or_insert(0) += 1;
        }

        let mut counts: Vec<_> = seen.into_values().collect();
        counts.sort_by(|a, b| b.cmp(a)); 

        let keep = k as usize;
        let sum_rest: i32 = counts.into_iter().skip(keep).sum();

        sum_rest
    }
}
