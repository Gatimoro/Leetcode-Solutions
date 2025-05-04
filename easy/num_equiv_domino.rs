use std::collections::HashMap;
impl Solution {
    pub fn num_equiv_domino_pairs(dominoes: Vec<Vec<i32>>) -> i32 {
        let mut count = HashMap::new();
        let mut tot = 0;
        for dom in dominoes{
            let k = (dom[0].min(dom[1]), dom[1].max(dom[0]));
            let seen = count.entry(k).or_insert(0);
            tot += *seen;
            *seen += 1;
        }
        tot
    }
}
// Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

// Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

