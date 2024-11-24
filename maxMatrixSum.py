class Solution:#this program calculates the maximum sum of the elements of a matrix where you can multiply by -1 any adjacent cell
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        suma=[]
        for x in matrix:
            for i in x:
                suma.append(i)
        suma=sorted(suma)
        x=2
        l=len(suma)
        while x<l+1:
            if suma[x-2]+suma[x-1]>=0:
                break
            x+=2
        return sum(suma[x-2:])-sum(suma[:x-2])
                
