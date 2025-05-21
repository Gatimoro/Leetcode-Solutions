// fill with zeroes every row and column that contains at least one zero.
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        let (mut fr, mut fc) = (false, false);
        for i in 0..matrix.len(){
            for j in 0..matrix[0].len(){
                if matrix[i][j] == 0{
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                    if i == 0{
                        fr = true;
                    }
                    if j == 0{
                        fc = true;
                    }
                }
            }
        }
        // for row in matrix.iter(){
        //     println!("{:?}", row);
        // }
        for i in 1..matrix.len(){
            for j in 1..matrix[0].len(){
                if matrix[0][j] == 0 || matrix[i][0] == 0{
                    matrix[i][j] = 0;
                }
            }
        }
        if fr{
            for i in 0..matrix[0].len(){
                matrix[0][i] = 0;
            }
        }
        if fc{
            for j in 0..matrix.len(){
                matrix[j][0] = 0;
            }
        }
    }
}
