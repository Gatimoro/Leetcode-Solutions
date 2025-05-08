// There is a dungeon with n x m rooms arranged as a grid.

// You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

// Return the minimum time to reach the room (n - 1, m - 1).

// Two rooms are adjacent if they share a common wall, either horizontally or vertically.
use std::collections::{HashSet, BinaryHeap};
use std::cmp::Reverse;
impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let mut visited = HashSet::new();
        let mut queue = BinaryHeap::new();
        let directions = [(1,0), (0,1), (-1,0), (0,-1)];
        let (m,n) = (move_time.len() as i32, move_time[0].len() as i32);
        queue.push(Reverse((0,0,0,1))); //(time, x, y, step)
        visited.insert((0,0));
        while let Some(Reverse((time, x, y, step))) = queue.pop(){
            for (dx, dy) in directions{
                let (nx, ny) = (x + dx, y + dy);
                if nx == -1 || ny == -1 || nx == m || ny == n || visited.contains(&(nx,ny)){
                    continue;
                }
                visited.insert((nx,ny));
                let nt = step + move_time[nx as usize][ny as usize].max(time);
                if nx == m - 1 && ny == n - 1{
                    return nt;
                }
                queue.push(Reverse((nt,nx,ny,3-step)));
            }
        }
        -1
    }
}
