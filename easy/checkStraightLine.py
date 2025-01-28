class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[0][0]-coordinates[1][0]==0:
            for x,_ in coordinates:
                if x!=coordinates[0][0]:
                    return False
            return True
        n=(coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        intersect=coordinates[0][1]-n*coordinates[0][0]
        for x,y in coordinates:
            if y!= x*n + intersect:
                return False
        return True
