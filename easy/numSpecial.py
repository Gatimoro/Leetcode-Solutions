# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r_sums, c_sums = [0] * len(mat), [0] * len(mat[0])
        for i, j in product(range(len(mat)), range(len(mat[0]))):
            r_sums[i] += mat[i][j]
            c_sums[j] += mat[i][j]
            # print(i,j)
        # print(r_sums, c_sums)
        return sum(1 for i, j in product(range(len(mat)), range(len(mat[0]))) if r_sums[i] == c_sums[j] == mat[i][j] == 1)
            
        
