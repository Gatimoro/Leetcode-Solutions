class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        ans=[]
        info = [len(matrix[0]),len(matrix),-1,-1] #outabounds right, down, left, up
        def trav(x,y,info,cur,ans):
            ans.append(matrix[x][y])
            nx, ny = x + directions[cur][0], y + directions[cur][1]
            if not(info[2] != ny != info[0] and info[3] != nx != info[1]):
                if cur==2 or cur==1: info[cur-1]-=1
                else: info[cur-1]+=1
                cur=(cur+1)%4
                nx, ny = x + directions[cur][0], y + directions[cur][1]
                if not(info[2] != ny != info[0] and info[3] != nx != info[1]):
                    return ans
            return trav(nx,ny,info,cur,ans)
        return trav(0,0,info,0,ans)
"""Return the elements of a matrix in spiral order"""
