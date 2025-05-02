impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        let n = dominoes.len();
        let mut time = i32::MAX;
        let (mut rightfall, mut leftfall) = (vec![i32::MAX; n], vec![i32::MAX; n]);
        let chars: Vec<char> = dominoes.chars().collect();

        for i in 0..n {
            if chars[i] == 'R' {
                time = 0;
            } else if chars[i] == 'L' {
                time = i32::MAX;
            }
            if time != i32::MAX {
                rightfall[i] = time;
                time += 1;
            }
        }


        time = i32::MAX;
        for i in (0..n).rev() {
            if chars[i] == 'L' {
                time = 0;
            } else if chars[i] == 'R' {
                time = i32::MAX;
            }
            if time != i32::MAX {
                leftfall[i] = time;
                time += 1;
            }
        }
        
        let mut ans = String::with_capacity(n);
        for i in 0..n {
            if rightfall[i] < leftfall[i] {
                ans.push('R');
            } else if leftfall[i] < rightfall[i] {
                ans.push('L');
            } else {
                ans.push(chars[i]);
            }
        }
        String::from(ans)
    }
}
// There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

// After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

// When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

// For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

// You are given a string dominoes representing the initial state where:

// dominoes[i] = 'L', if the ith domino has been pushed to the left,
// dominoes[i] = 'R', if the ith domino has been pushed to the right, and
// dominoes[i] = '.', if the ith domino has not been pushed.
// Return a string representing the final state.

