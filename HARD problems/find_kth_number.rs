// Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 
impl Solution {
    pub fn find_kth_number(n: i32, mut k: i32) -> i32 {
        let (n, mut cur) = (n as i64, 1_i64);
        k -= 1;

        fn count_steps(mut prefix: i64, n: i64) -> i64 {
            let mut steps = 0;
            let mut next = prefix + 1;
            while prefix <= n {
                steps += (n + 1).min(next) - prefix;
                prefix *= 10;
                next *= 10;
            }
            steps
        }

        while k > 0 {
            let steps = count_steps(cur, n);
            if steps <= k as i64 {
                cur += 1;
                k -= steps as i32;
            } else {
                cur *= 10;
                k -= 1;
            }
        }

        cur as i32
    }
}
