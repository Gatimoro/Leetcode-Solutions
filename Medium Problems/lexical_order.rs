// Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

// You must write an algorithm that runs in O(n) time and uses O(1) extra space. 


impl Solution {
    pub fn lexical_order(n: i32) -> Vec<i32> {
        let mut ans = Vec::with_capacity(n as usize);
        fn go_next(stack: &mut Vec<i32>, maximum: i32, mut cur: i32){
            if cur > maximum {
                return
            }
            stack.push(cur);
            cur *= 10;
            for n in 0..10 as i32{
                go_next(stack, maximum, cur + n);
            }
        }
        for s in 1..10 as i32{
            go_next(&mut ans, n, s);
        }
        ans
    }
}

