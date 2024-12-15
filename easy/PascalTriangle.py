class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        while numRows-1:
            row=[1]
            for i in range(len(ans[-1])-1):
                row.append(ans[-1][i]+ans[-1][i+1])
            row.append(1)
            ans.append(row)
            numRows-=1
        return ans
