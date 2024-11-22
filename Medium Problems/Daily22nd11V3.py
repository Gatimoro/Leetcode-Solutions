class Solution:#This is a better approach for calculating the maximum amount of equal rows after flipping some columns in a matrix.
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        #first notice that you can just flip the rows
        m=len(matrix)
        bins=[]
        diffs=Counter()
        ans=0
        for i in range(m):
            #to avoid duplicates from the prev program, I made it so that each pattern is only flipped if it starts with 0.
            if matrix[i][0]:
                bins.append(matrix[i])
            else:
                bins.append([1-x for x in matrix[i]])
            #diffs counts the different patterns
            diffs[tuple(bins[-1])]+=1
        return max(diffs.values())
        
