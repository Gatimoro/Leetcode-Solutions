class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points,key = lambda x: (x[0]*x[0] + x[1]*x[1])**0.5 )[:k]
"""Find k closest points to origin in a 2d plane."""
