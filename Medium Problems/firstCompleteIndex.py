class Solution: """a lot of comments because I got 99%+ and wanted to share the solution"""
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        #We will initialize 2 arrays to contain the row and column of each number
        row_of_=[0]*(len(arr)+1)
        col_of_=[0]*(len(arr)+1)
        
        #then fill the arrays with the corresponding row and col index for each element
        for row_index, row in enumerate(mat):
            for col_index, element in enumerate(row):
                row_of_[element] = row_index
                col_of_[element] = col_index
        #print(row_of_,'\n',col_of_) #as you can see, at each index is stored the row/col of said index.
        
        #now we need to keep track of how many elements remain unseen in each row and column
        remaining_in_row = [len(mat[0])] * len(mat) #each row contains len(row) elements and we have len(mat) rows
        remaining_in_col = [len(mat)] * len(mat[0]) #and viceversa for the columns

        #we now iterate through the array and update the remaining values in each row and col
        for i, number in enumerate(arr):
            remaining_in_row[row_of_[number]]-=1 
            remaining_in_col[col_of_[number]]-=1
            
            #when we find all the elements in the row or col, we return the index of the number we are checking.
            if remaining_in_row[row_of_[number]]==0 or remaining_in_col[col_of_[number]]==0:
                return i
"""You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat."""
