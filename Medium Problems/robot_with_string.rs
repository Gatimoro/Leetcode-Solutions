// You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

// Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
// Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
// Return the lexicographically smallest string that can be written on the paper.

impl Solution {
    pub fn robot_with_string(s: String) -> String {
        let n = s.len();
        let mut bytes = s.into_bytes();

        let mut smallest_in_front = vec![0;n + 1];
        let mut cur = u8::MAX;
        for i in (0..n).rev(){
            smallest_in_front[i] = cur;
            cur = cur.min(bytes[i]);
        }
        let mut t = Vec::with_capacity(n);
        let mut ans = Vec::with_capacity(n);
        for (letter, smallest) in bytes.into_iter().zip(smallest_in_front.into_iter()){
            t.push(letter);
            while let Some(&next) = t.last(){
                if next <= smallest{
                    ans.push(t.pop().unwrap());
                }else{
                    break;
                }
            }
        }
        unsafe {String::from_utf8_unchecked(ans)}
    }
}
