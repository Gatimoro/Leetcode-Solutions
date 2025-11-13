// You are given a binary string s.

// You can perform the following operation on the string any number of times:

// Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
// Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
// Return the maximum number of operations that you can perform.

impl Solution {
    pub fn max_operations(s: String) -> i32 {
        let mut seen = 0;
        let mut opsss = 0;
        let mut last = '1';
        for n in s.chars(){
            if n == '1'{
                seen += 1;
            }else if n=='0' && last != '0'{
                opsss += seen;   
            }
            last = n;
        }opsss
    }
}
