class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        dias = [[] for _ in range((2*len(grid)-1))]
        leng=len(grid)
        dec = [[] for x in range(leng)]
        inc = [[] for x in range(leng-1)]
        for i in range(leng-1,-1,-1):
            x=i
            for c in range(leng-i):
                dec[leng-1-i].append(grid[x][c])
         
                x+=1

        for i in range(1,leng):
            x=i
            for c in range(leng-i):
                inc[i-1].append(grid[c][x])
      
                x+=1
        for ind in range(len(inc)):
            inc[ind].sort()
            dec[ind].sort(reverse=True)
        dec[-1].sort(reverse=True)
  
        for i in range(leng-1,-1,-1):
            x=i
            for k,c in enumerate(range(leng-i)):
                grid[x][c]=dec[leng-1-i][k]
                x+=1
        for i in range(1,leng):
            x=i
            for k,c in enumerate(range(leng-i)):
                
                grid[c][x]=inc[i-1][k]
 
                x+=1
        return(grid)
        
"""Sort matrix's lower left triangle in decreasing order and top right in increasing"""
