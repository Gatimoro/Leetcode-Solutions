use std::collections::HashMap;
impl Solution {
    pub fn fair_candy_swap(alice_sizes: Vec<i32>, bob_sizes: Vec<i32>) -> Vec<i32> {
        let a_tot:i32 = alice_sizes.iter().sum();
        let b_tot:i32 = bob_sizes.iter().sum();
        let diff = (b_tot - a_tot);
        let mut compl = HashMap::new();
        for a in alice_sizes.into_iter(){
            *compl.entry(diff + a * 2).or_insert(0) = a as i32; 
        }
        for a in bob_sizes.into_iter(){
            let e = compl.get(&(a * 2)).unwrap_or(&-1);
            if e != &-1{
                return vec![*e, a as i32];
            }
        }
        vec![0,0]
    }
}
