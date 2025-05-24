// Given a string s, find the sum of the 3 largest unique prime numbers that can be formed using any of its substrings.

// Return the sum of the three largest unique prime numbers that can be formed. If fewer than three exist, return the sum of all available primes. If no prime numbers can be formed, return 0.

// A prime number is a natural number greater than 1 with only two factors, 1 and itself.

// A substring is a contiguous sequence of characters within a string.

// Note: Each prime number should be counted only once, even if it appears in multiple substrings. Additionally, when converting a substring to an integer, any leading zeros are ignored.


impl Solution {
    pub fn sum_of_largest_primes(s: String) -> i64 {
        fn isprime(n: i64) -> bool{
            if n < 2{
                return false;
            }
            if n == 2{
                return true;
            }
            if n%2 == 0{
                return false;
            }
            let mut div = 3;

            while div * div <= n{
                if n % div == 0{
                    return false;
                }div += 1;
            }
            return true;
        }
        let b = s.as_bytes();
        let mut primes = vec![0,0,0];
        for start in 0..s.len(){
            for end in start + 1..=s.len(){
                if let Ok(sub) = std::str::from_utf8(&b[start..end]){
                    if let Ok(num) = sub.parse::<i64>(){
                        if isprime(num){
                            primes.push(num);

                        }
                    }
                }
            }
        }
        primes.sort_unstable_by(|a, b| b.cmp(a));
        primes.dedup();
        primes.iter().take(3).sum()
    }
}
