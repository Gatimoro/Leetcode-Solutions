impl Solution {
    pub fn count_good_strings(low: i32, high: i32, zero: i32, one: i32) -> i32 {
        let (low, high, zero, one) = (
            low as usize,
            high as usize,
            zero as usize,
            one as usize
        );

        let mut dp = vec![0u64; high + 1];
        dp[0] = 1;
        let mut total = 0u64;
        let MOD = 1_000_000_007u64;

        for i in 1..=high {
            if i >= zero {
                dp[i] = (dp[i] + dp[i - zero]) % MOD;
            }
            if i >= one {
                dp[i] = (dp[i] + dp[i - one]) % MOD;
            }
            if i >= low {
                total = (total + dp[i]) % MOD;
            }
        }

        total as i32
    }
}

// Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

// Append the character '0' zero times.
// Append the character '1' one times.
// This can be performed any number of times.

// A good string is a string constructed by the above process having a length between low and high (inclusive).

// Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
