# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [sum(int(element) << i for i, element in enumerate(row)) for row in matrix]
        # print(matrix)
        width, biggest = 1, 0
        while any(matrix):
            square_size = 0
            # print(matrix)
            next_matrix = [e1 & e2 for e1, e2 in pairwise(matrix)]
            while any(matrix):
                square_size += 1
                # print('next')
                # for r in matrix:
                #     print(bin(r)[2:])
                matrix = [(r >> 1) & r for r in matrix]
                
            biggest = max(biggest, width * square_size)
            matrix = next_matrix
            width += 1
        return biggest
            
