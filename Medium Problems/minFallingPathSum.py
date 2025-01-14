class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1,len(matrix)):
            lung=deque(matrix[row-1][:2])
            matrix[row][0]+=min(lung)
            for col in range(2,len(matrix)):
                lung.append(matrix[row-1][col])
                matrix[row][col-1]+=min(lung)
                lung.popleft()
            matrix[row][-1]+=min(lung)
        return min(matrix[-1])
"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)."""
