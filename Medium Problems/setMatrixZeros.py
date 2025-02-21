class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = [False] * len(matrix[0])
        rows = [False] * len(matrix)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not matrix[row][col]:
                    rows[row] = True
                    cols[col] = True
            
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place."""
