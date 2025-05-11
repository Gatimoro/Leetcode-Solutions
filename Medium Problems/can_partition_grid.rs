// You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

// Each of the two resulting sections formed by the cut is non-empty.
// The sum of the elements in both sections is equal.
// Return true if such a partition exists; otherwise return false.©leetcode
impl Solution {
    pub fn can_partition_grid(grid: Vec<Vec<i32>>) -> bool {
        let mut rows = vec![0;grid.len()];
        let mut cols = vec![0;grid[0].len()];
        for (r, row) in grid.iter().enumerate(){
            for (c, &col) in row.iter().enumerate(){
                rows[r] += col as i64;
                cols[c] += col as i64;
            } 
        }
        let mut target = rows.iter().sum();
        if target %2 == 1{
            return false;
        }
        // println!("{}", target);
        target /= 2;
        let mut cur = 0;
        for elem in rows{
            cur += elem;
            if cur == target{
                return true;
            }else if cur > target{
                break;
            }
        }
        cur = 0;
        for elem in cols{
            cur += elem;
            if cur == target{
                return true;
            }else if cur > target{
                return false;
            }
        }
        false
    }       
}©leetcode
