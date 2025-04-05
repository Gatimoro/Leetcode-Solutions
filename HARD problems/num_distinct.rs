//First Hard using rust, altho this one wasn't too hard.
impl Solution {
    pub fn num_distinct(s: String, t: String) -> i32 {
        let leng = t.len() + 1;
        let t_letters: Vec<char> = t.chars().collect();
        let mut combs = vec![0; leng];
        combs[0] = 1; //1 combination of length 0
        for s_letter in s.chars(){
            for index in (1..leng).rev(){
                if s_letter ==t_letters[index-1]{
                    combs[index] += combs[index-1];
                }
            }
        }
        combs[leng-1]

        
    }
}
//Given two strings s and t, return the number of distinct subsequences of s which equals t.

//The test cases are generated so that the answer fits on a 32-bit signed integer.
