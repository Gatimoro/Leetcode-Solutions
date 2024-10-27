class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m=0
        side=2
        squares=0
        prov=0
        max=0
        for o in matrix:
            squares+=sum(o)
            m+=1
            for p in o:
                if p==1:
                    prov+=1
                else:
                    if max<prov:
                        max=prov
                    prov=0
        n=len(matrix[0])
        while not side>m and not side>n and side<=max:
            
            for row in range(m-side+1):
                for col in range(n-side+1):
                    found=True
                    for line in range(side):
                        if 0 in matrix[row+line][col:side+col]:
                            found=False
                            break
                    if found:
                        squares+=1
            side+=1
        return squares
