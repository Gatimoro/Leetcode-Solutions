use std::collections::HashMap;
impl Solution {
    pub fn count_largest_group(n: i32) -> i32 {
        fn digitsum(mut x: i32) -> i32{
            let mut ret = 0;
            while x != 0{
                ret += x % 10;
                x /= 10;
            }ret
        }
        let mut longest = 0;
        let mut count_of_largest = 0;
        let mut appearences = HashMap::new();
        for num in 1..=n{
            // println!("{}",n);
            let g = appearences.entry(digitsum(num)).or_insert(0);
            *g += 1;
            // println!("{}, {}",digitsum(num), n);
            if *g == longest{
                count_of_largest += 1;
            }else if *g > longest{
                count_of_largest = 1;
                longest = *g;
            }
        }count_of_largest
        
    }
}
// You are given an integer n.

// Each number from 1 to n is grouped according to the sum of its digits.

// Return the number of groups that have the largest size.
