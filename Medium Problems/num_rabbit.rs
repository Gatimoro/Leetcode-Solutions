use std::collections::HashMap;
impl Solution {
    pub fn num_rabbits(answers: Vec<i32>) -> i32 {
        let mut amount = HashMap::new();
        let mut count = 0;
        for color in answers.into_iter(){
            *amount.entry(color).or_insert(0) += 1;
            let mut am = amount.get_mut(&color).unwrap();
            if *am == 1{
                count += color + 1;
            }
            if *am > color{
                *am = 0;
            }
        }count
    }
}
// There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

// Given the array answers, return the minimum number of rabbits that could be in the forest.
