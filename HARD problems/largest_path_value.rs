// There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

// You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

// A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

// Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.
use std::collections::HashMap;
impl Solution {
    pub fn largest_path_value(colors: String, edges: Vec<Vec<i32>>) -> i32 {

        let mut indeg = vec![0; colors.len()];
        let mut forward = vec![vec![]; colors.len()];
        let mut visited = vec![false; colors.len()];
        let mut wasHereBefore = HashMap::new();
        let colors = colors.as_bytes();
        
        
        for c in edges{
            let (a, b) = (c[0] as usize, c[1] as usize);
            forward[a].push(b as usize);
            indeg[b] += 1;
        }
        
        let mut ansa = 0;
        fn dfs(indeg: &mut Vec<i32>, tree: &Vec<Vec<usize>>, mut state: [i32; 26], node: usize, visited: &mut Vec<bool>, wasHereBefore: &mut HashMap<usize, [i32;26]>, colors: &[u8], ansa: &mut i32){
            if indeg[node] != 0{
                let mut entry = wasHereBefore.entry(node).or_insert([0i32;26]);
                for (a, b) in entry.iter_mut().zip(state.iter()) {
                    *a = (*a).max(*b);
                }
            }else{
                if visited[node]{
                    return
                }
                visited[node] = true;
                if let Some(entry) = wasHereBefore.get(&node){
                    
                    for (a, b) in state.iter_mut().zip(entry.iter()) {
                        *a = (*a).max(*b);
                    }
                }
                let mut next_state = state;
                next_state[(colors[node] - b'a') as usize] += 1;
                
                if tree[node].is_empty(){
                    // println!("{:?}", state);
                    *ansa = (*ansa).max(*next_state.iter().max().unwrap());
                }else{
                    for &friend in tree[node].iter(){
                        indeg[friend] -= 1;
                        dfs(indeg, tree, next_state, friend, visited, wasHereBefore, colors, ansa)
                    }
                }
            }
            // println!("after node {}, {:?}",node,  indeg);
        }
        for start in 0..colors.len(){
            if indeg[start] == 0{
                dfs(&mut indeg, &forward, [0;26], start, &mut visited, &mut wasHereBefore, &colors, &mut ansa)
            }
        }
        if visited.into_iter().all(|x| x) {ansa} else {-1}
    }
}


