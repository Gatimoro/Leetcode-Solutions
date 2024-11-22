class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
      #This problem calculates the maximum amount equal rows after inverting some amount of columns by using the fact that you can just invert the rows.
        m=len(matrix)
        bins=[]
        diffs=[]
        ans=0
        for i in range(m):
            bins.append(matrix[i])
            if not matrix[i] in diffs:
                diffs.append(matrix[i])
            inverted=[1-x for x in matrix[i]]
            bins.append(inverted)
            if not inverted in diffs:
                diffs.append(inverted)
        for k in range(len(diffs)):
            count=bins.count(diffs[k])
            if count>ans:
                ans=count
        return ans
        
