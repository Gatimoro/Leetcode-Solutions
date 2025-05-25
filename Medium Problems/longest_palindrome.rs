// You are given an array of strings words. Each element of words consists of two lowercase English letters.

// Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

// Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

// A palindrome is a string that reads the same forward and backward.

 
//V2
impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        let mut singles = 0i32;
        let mut length = 0i32;
        let mut pair = [0; 26 * 26];
        for word in words{
            let bytez = word.as_bytes();
            let (a, b) = ((bytez[0] - b'a') as usize, (bytez[1] - b'a') as usize);
            let idx = a * 26 + b;
            if pair[idx] == 0{
                let compliment = b * 26 + a;
                pair[compliment] += 1;
                if a==b{
                    singles += 1;
                }
            }else{
                pair[idx] -= 1;
                length += 1;
                if a==b{
                    singles -= 1;
                }
            }
        }
        (length << 2) + (((singles != 0) as i32)<<1)
    }
}
//V1
impl Solution {
    pub fn longest_palindrome(words: Vec<String>) -> i32 {
        let mut singles = 0i32;
        let mut length = 0i32;
        let mut pair = [0; 26 * 26];
        for word in words{
            let bytez = word.as_bytes();
            let (a, b) = ((bytez[0] - b'a') as usize, (bytez[1] - b'a') as usize);
            let idx = a * 26 + b;
            if a == b{
                if pair[idx] == 0{
                    singles += 1;
                }else{
                    singles -= 1;
                    length += 1
                }
                pair[idx] ^= 1;
            }else{
                if pair[idx] == 0{
                    let compliment = b * 26 + a;
                    pair[compliment] += 1
                }else{
                    pair[idx] -= 1;
                    length += 1;
                }
            }
        }
        (length << 2) + (((singles != 0) as i32)<<1)
    }
}
