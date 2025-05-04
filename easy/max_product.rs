impl Solution {
    pub fn max_product(mut n: i32) -> i32 {
        let mut max = 0;
        let mut best = 0;
        while n != 0{
            best = best.max((n%10) * max);
            max = max.max(n%10);
            n /= 10;
        }
        best


    }
}
// You are given a positive integer n.

// Return the maximum product of any two digits in n.

// Note: You may use the same digit twice if it appears more than once in n.

 
