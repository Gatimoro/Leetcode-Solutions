// You are given an undirected graph of n nodes, numbered from 0 to n - 1. Each node is connected to at most 2 other nodes.

// The graph consists of m edges, represented by a 2D array edges, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi.

// You have to assign a unique value from 1 to n to each node. The value of an edge will be the product of the values assigned to the two nodes it connects.

// Your score is the sum of the values of all edges in the graph.

// Return the maximum score you can achieve.©leetcode
impl Solution {
    pub fn max_score(n: i32, edges: Vec<Vec<i32>>) -> i64 {
        let mut visited = vec![false; n as usize];
        let mut total = 0i64;
        let mut cons = vec![vec![];n as usize];
        for edge in edges {
            let s = edge[0] as usize;
            let e = edge[1] as usize;
            cons[s].push(e);
            cons[e].push(s);
        }

        
        fn travel(node: usize, visited: &mut Vec<bool>, cons: &Vec<Vec<usize>>) -> (i64, bool){
            match cons[node].len() {
                1 => {
                    if !visited[cons[node][0]]{
                        visited[cons[node][0]] = true;
                        let (d, _) = travel(cons[node][0], visited, cons );
                        (1 + d, false)
                    }else{
                        (1, false)
                    }
                }
                2 => {
                    if visited[cons[node][0]] && visited[cons[node][1]]{
                        (1 , true)
                    }else if !(visited[cons[node][0]] || visited[cons[node][1]]){
                        visited[cons[node][0]] = true;
                        let (d1, st1) = travel(cons[node][0], visited, cons );
                        if !visited[cons[node][1]]{
                            visited[cons[node][1]] = true;
                            let (d2, st2) = travel(cons[node][1], visited, cons );
                            (d1 + d2 + 1, st1 || st2)
                        }else{
                            (d1 + 1, st1)
                        }
                    }else{
                        if !visited[cons[node][0]]{
                            visited[cons[node][0]] = true;
                            let (d, st) = travel(cons[node][0], visited, cons );
                            (1 + d, st)
                        }else{
                            visited[cons[node][1]] = true;
                            let (d, st) = travel(cons[node][1], visited, cons );
                            (d + 1, st)
                        }
                    }
                }
                _ => {
                    (1 , false)
                }
            }
        }
        
        let mut cycles = Vec::new();
        let mut paths = Vec::new();
        for start in 0..n as usize{
            if !visited[start]{
                visited[start] = true;
                let (depth, cycle) = travel(start, &mut visited, &cons);
                if cycle{
                    cycles.push(depth)
                }else{
                    paths.push(depth);
                }
            }
        }
        let mut n  = n as i64;
        cycles.sort();
        paths.sort_by(|a, b| b.cmp(a));
        // println!("{:?} {:?}", cycles, paths);
        for cycle in cycles{
            total += n * (n-1);
            // println!("{} * {} -> {}", n, n-1, total);
            for x in (n-cycle+1..n-1).rev(){
                total += x * (x + 2);
                // println!("{} * {} -> {}", x, x+2, total);
            }
            n -= cycle;
            total += (n+1) * (n+2);
            // println!("{} * {}", n+1, n+2);
        }
        for path in paths{
            if path == 1{
                break;
            }
            total += n * (n-1);
            // println!("{} * {} -> {}", n, n-1, total);
            for x in (n-path+1..n-1).rev(){
                total += x * (x + 2);
                // println!("{} * {} -> {}", x, x + 2, total);
            }
            n -= path;
            // println!("n is now {}", n);
        }
        total
    }
}
