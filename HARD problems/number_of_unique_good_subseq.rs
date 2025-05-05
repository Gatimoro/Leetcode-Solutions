impl Solution {
    pub fn number_of_unique_good_subsequences(binary: String) -> i32 {
        let chars: Vec<char> = binary.chars().collect();
        let mut seen_a_zero = false;
        let (mut zero, mut one) = (0u64, 0u64);
        let MOD = 1_000_000_007u64;
        for c in chars.into_iter(){
            let its_a_zero = c=='0';
            seen_a_zero |= its_a_zero; 
            if its_a_zero{
                zero = (zero + one) % MOD;
            }else{
                one = (zero + one + 1) % MOD;
            }
        }
        ((zero + one + seen_a_zero as u64) % MOD)as i32
    }
}
// You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").

// Find the number of unique good subsequences of binary.

// For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
// Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.

// A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
