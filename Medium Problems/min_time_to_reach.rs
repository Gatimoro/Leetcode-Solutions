use std::collections::BinaryHeap;

#[derive(Eq, PartialEq)]
struct Position {
    x: i32,
    y: i32,
    time: i32,
}

impl Ord for Position {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        other.time.cmp(&self.time)  // min-heap
    }
}

impl PartialOrd for Position {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

impl Solution {
    pub fn min_time_to_reach(move_time: Vec<Vec<i32>>) -> i32 {
        let directions = [(1, 0), (0, 1), (-1, 0), (0, -1)];
        let mut heap = BinaryHeap::new();
        heap.push(Position { x: 0, y: 0, time: 0 });
        let (m, n) = (move_time.len(), move_time[0].len());
        let mut visited = vec![vec![false; n]; m];
        visited[0][0] = true;

        while let Some(position) = heap.pop() {
            for (dx, dy) in directions {
                let (nx, ny) = (position.x + dx, position.y + dy);
                if nx < 0 || nx >= m as i32 || ny < 0 || ny >= n as i32 { continue; }
                let (nx, ny) = (nx as usize, ny as usize);

                if visited[nx][ny] { continue; }
                visited[nx][ny] = true;

                let t = 1 + move_time[nx][ny].max(position.time);
                if nx == m - 1 && ny == n - 1 { return t; }
                heap.push(Position { x: nx as i32, y: ny as i32, time: t });
            }
        }
        -1
    }
}
// There is a dungeon with n x m rooms arranged as a grid.

// You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

// Return the minimum time to reach the room (n - 1, m - 1).

// Two rooms are adjacent if they share a common wall, either horizontally or vertically.
