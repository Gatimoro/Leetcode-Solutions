class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        bins=[]
        diffs=[]
        ans=0
        for i in range(m):
            if matrix[i][0]:
                bins.append(matrix[i])
            else:
                bins.append([1-x for x in matrix[i]])
            if bins[-1] not in diffs:
                diffs.append(bins[-1])
        for k in diffs:
            count=bins.count(k)
            if count>ans:
                ans=count
        return ans
        
