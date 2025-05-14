// You are given a string s consisting of lowercase English letters, an integer t representing the number of transformations to perform, and an array nums of size 26. In one transformation, every character in s is replaced according to the following rules:

// Replace s[i] with the next nums[s[i] - 'a'] consecutive characters in the alphabet. For example, if s[i] = 'a' and nums[0] = 3, the character 'a' transforms into the next 3 consecutive characters ahead of it, which results in "bcd".
// The transformation wraps around the alphabet if it exceeds 'z'. For example, if s[i] = 'y' and nums[24] = 3, the character 'y' transforms into the next 3 consecutive characters ahead of it, which results in "zab".
// Return the length of the resulting string after exactly t transformations.

// Since the answer may be very large, return it modulo 109 + 7.


const MOD: i64 = 1_000_000_007;
impl Solution {
    pub fn length_after_transformations(s: String, t: i32, nums: Vec<i32>) -> i32 {
        let mut T = [[0i64;26];26];
        let mut quanta = [0i64;26];
        for c in s.chars(){
            let c = c as usize - 'a' as usize;
            quanta[c] += 1;
        }
        for (i, n) in nums.into_iter().enumerate(){
            let n = n as usize;
            for nc in i + 1 ..= i + n { T[nc % 26][i] = 1; }
        }
        // for &r in T.iter(){println!("{:?}", r)}
        //     println!("");
        T = Self::binary_exp(&T, t as i64);
        T.into_iter().fold(0, |tot, row| {
            let dot = row.into_iter()
                         .enumerate()
                         .fold(0, |r, (i, x)| (r + x * quanta[i]) % MOD);
            (tot + dot) % MOD
        }) as i32
    }

    fn multiply(C: &[[i64; 26];26], Z: &[[i64; 26];26]) -> [[i64;26];26]{
        let mut result = [[0i64; 26];26];
        for row in 0..26{
            for col in 0..26{
                for i in 0..26{
                    result[row][col] = ( result[row][col] + (C[row][i] * Z[i][col]) %MOD ) % MOD;
                }
            }
        }
        result
    }
    
    fn binary_exp(M1: &[[i64;26];26], mut exp: i64) -> [[i64;26];26]{
        let mut R = [[0i64; 26]; 26];
        for i in 0..26 { R[i][i] = 1; }
        let mut base = M1.clone();
        while exp > 0{
            if exp %2 == 1{
                R = Self::multiply(&R, &base);
            }
            base = Self::multiply(&base, &base);
            exp >>= 1;
        }
        R
    }
}
