use std::collections::HashMap;
impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        let mut groups = HashMap::new();
        let mut ans: Vec<Vec<i32>> = Vec::new();
        for (i, peep )in group_sizes.into_iter().enumerate(){
            let peep = peep as usize;
            let group = groups.entry(peep).or_insert(Vec::with_capacity(peep));
            group.push(i as i32);
            if group.len() == peep{
                ans.push(group.clone());
                group.clear();
            }
        }ans
    }
}
// There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

// You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

// Return a list of groups such that each person i is in a group of size groupSizes[i].

// Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

