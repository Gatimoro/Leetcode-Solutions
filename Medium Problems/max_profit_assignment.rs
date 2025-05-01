impl Solution {
    pub fn max_profit_assignment(difficulty: Vec<i32>, profit: Vec<i32>, mut worker: Vec<i32>) -> i32 {
        let mut pairs = difficulty.into_iter().zip(profit.into_iter()).collect::<Vec<_>>();
        pairs.sort_unstable_by_key(|&(d, p)| (d, p)); // sort by difficulty, then profit
        worker.sort_unstable();

        let (mut best, mut total) = (0, 0);
        let mut i = 0;

        for w in worker {
            while i < pairs.len() && pairs[i].0 <= w {
                best = best.max(pairs[i].1);
                i += 1;
            }
            total += best;
        }

        total
    }
}
// You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

// difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
// worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
// Every worker can be assigned at most one job, but one job can be completed multiple times.

// For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
// Return the maximum profit we can achieve after assigning the workers to the jobs.
