// You are given a string array words, and an array groups, both arrays having length n.

// The hamming distance between two strings of equal length is the number of positions at which the corresponding characters are different.

// You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik-1] having length k, the following holds:

// For adjacent indices in the subsequence, their corresponding groups are unequal, i.e., groups[ij] != groups[ij+1], for each j where 0 < j + 1 < k.
// words[ij] and words[ij+1] are equal in length, and the hamming distance between them is 1, where 0 < j + 1 < k, for all indices in the subsequence.
// Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

// Note: strings in words may be unequal in length.


impl Solution {
    pub fn get_words_in_longest_subsequence(words: Vec<String>, groups: Vec<i32>) -> Vec<String> {
        let mut double_penetration: Vec<_> = (0..words.len()).map(|x| (x, 1)).collect();
        fn valid(a: &String, b: &String) -> bool{
            let mut ham = 0;
            if a.len() == b.len(){
                for (f,s) in a.chars().zip(b.chars()){
                    ham += (f != s) as i32;
                }
            }
            ham == 1
        }
        fn build_ans(words: &Vec<String>, dp: &Vec<(usize, i32)>, cur: usize) -> Vec<String>{
            if dp[cur].0 == cur{
                vec![words[cur].clone()]
            }else{
                let mut ret = build_ans(words, dp, dp[cur].0);
                ret.push(words[cur].clone());
                ret
            }
        }

        let mut reti = (0, 1);
        for i in 0..words.len(){
            for j in 0..i{
                if groups[i] != groups[j] && valid(&words[i], &words[j]) && double_penetration[j].1 >= double_penetration[i].1 {
                    double_penetration[i] = (j, double_penetration[j].1 + 1);
                }
            }
            if double_penetration[i].1 > reti.1{
                reti = (i, double_penetration[i].1);
            }
        }
        println!("{:?}", double_penetration);
        build_ans(&words, &double_penetration, reti.0)
        
    }
}

