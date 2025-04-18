impl Solution {
    pub fn count_and_say(n: i32) -> String {
        let mut cur = vec![1].into_iter();
        let mut count = 0;
        let mut prev_char = 0;
        for _ in 1..n{
            let mut next = Vec::new();
            prev_char = cur.next().unwrap();
            count = 1;
            for c in cur.into_iter(){
                if prev_char == c{
                    count+=1;
                }else{
                    next.push(count);
                    count = 1;
                    next.push(prev_char);
                    prev_char = c;
                }
            }
            next.push(count);
            next.push(prev_char);
            cur = next.into_iter();
        }cur.map(|x| x.to_string()).collect::<String>()
    }
}
// The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

// countAndSay(1) = "1"
// countAndSay(n) is the run-length encoding of countAndSay(n - 1).
// Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

// Given a positive integer n, return the nth element of the count-and-say sequence.

