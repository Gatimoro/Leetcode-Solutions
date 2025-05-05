impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        const MOD: u64 = 1_000_000_007; 
        let (mut cur, mut prev, mut sum) = (1u64, 0u64, 0u64);
        for _ in 0..n {
            let hold = cur;
            cur = (cur + prev + sum) % MOD;
            let new_sum = (sum + 2 * prev) % MOD;
            prev = hold;
            sum = new_sum;
        }
        cur as i32
    }
}
// You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

// Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

// In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
