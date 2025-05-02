impl Solution {
    pub fn min_reorder(n: usize, connections: Vec<Vec<i32>>) -> i32 {
        let mut free = vec![vec![]; n];
        let mut p2w = vec![vec![]; n];
        let mut visited = vec![false; n];
        for a in connections{
            free[a[0] as usize].push(a[1] as usize);
            p2w[a[1] as usize].push(a[0] as usize);
        }
        visited[0] = true;
        let mut stack:Vec<usize> = vec![0];
        let mut ans = 0;
        while let Some(cur) = stack.pop(){
            for &neighbor in p2w[cur].iter(){
                if !visited[neighbor]{
                    stack.push(neighbor);
                    visited[neighbor] = true;
                    ans += 1
                }       
            }
            for &neighbor in free[cur].iter(){
                if !visited[neighbor]{
                    stack.push(neighbor);
                    visited[neighbor] = true;
                }       
            }
        }
        ans
    }
}

// There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

// Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

// This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

// Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

// It's guaranteed that each city can reach city 0 after reorder.
