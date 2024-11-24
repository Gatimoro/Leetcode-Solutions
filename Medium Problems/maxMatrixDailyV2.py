class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        suma=[]
        tot=0
        for x in matrix:
            for i in x:
                suma.append(i)
        suma=sorted(suma)
        x=2
        l=len(suma)
        while x<=l:
            cur = suma[x-1]+suma[x-2]
            if cur>=0:
                tot+=cur
            else:
                tot-=cur
            x+=2
        if l%2:
            return tot+suma[x-2]
        return tot
                
