// You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.

// While there is a '*', do the following operation:

// Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
// Return the lexicographically smallest resulting string after removing all '*' characters.
use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(PartialEq, Debug, Eq)]
struct Character{
    letter: u8,
    idx: usize,
}


impl Ord for Character{
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        match other.letter.cmp(&self.letter){
            Ordering::Equal => self.idx.cmp(&other.idx),
            ord => ord,
        }
    }
}

impl PartialOrd for Character{
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn clear_stars(s: String) -> String {
        let n = s.len();
        let bytes = s.into_bytes();
        let mut is_excluded = vec![false; n];
        let mut hip: BinaryHeap<Character> = BinaryHeap::new();
        for i in 0..n{
            let b = bytes[i];
            if b == b'*'{
                is_excluded[i] = true; 
                if let Some(letter)  = hip.pop(){
                    is_excluded[letter.idx] = true;
                }
            }else{
                hip.push(Character{letter: b, idx: i});
            }
        }
        let ret:Vec<_> = bytes.into_iter().enumerate().filter_map(|(i, x)| if !is_excluded[i]{ Some(x) } else {None}).collect();
        unsafe { String::from_utf8_unchecked(ret) }
    }
}

