// There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 0-indexed 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree. You are also given a positive integer k, and a 0-indexed array of non-negative integers nums of length n, where nums[i] represents the value of the node numbered i.

// Alice wants the sum of values of tree nodes to be maximum, for which Alice can perform the following operation any number of times (including zero) on the tree:

// Choose any edge [u, v] connecting the nodes u and v, and update their values as follows:
// nums[u] = nums[u] XOR k
// nums[v] = nums[v] XOR k
// Return the maximum possible sum of the values Alice can achieve by performing the operation any number of times.


impl Solution {
    pub fn maximum_value_sum(nums: Vec<i32>, k: i32, edges: Vec<Vec<i32>>) -> i64 {
        let mut total = nums.iter().map(|&x| x as i64).sum();
        let mut profit: Vec<i64> = nums.into_iter().map(|x| (x ^ k) as i64 - x as i64).collect();
        profit.sort_unstable();
        while let Some(a) = profit.pop(){
            if a <= 0{break;}
            if let Some(b) = profit.pop(){
                let c = a + b;
                if c > 0{
                    total += c;
                }
            }
        }
        total
    }
}
