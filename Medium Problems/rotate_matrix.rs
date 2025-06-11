// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let n = matrix.len();

        for i in 0..n{
            for j in i + 1..n{
                matrix[i][j] ^= matrix[j][i];
                matrix[j][i] ^= matrix[i][j];
                matrix[i][j] ^= matrix[j][i];
            }
        }
        for row in matrix.iter_mut(){
            println!("{:?}", row);
            for i in 0..n/2{
                row[n - 1 - i] ^= row[i];
                row[i] ^= row[n - i - 1];
                row[n - i - 1] ^= row[i];
            }
            println!("{:?}", row);
        }
    }
}
