# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def dist(a, aa, b, bb):
            return (abs(a - b)**2 + abs(aa - bb)**2)**0.5
        def area(a, b, c):
            (a1, a2), (b1, b2), (c1, c2) = a, b, c
            A, B, C = dist(a1, a2, b1, b2), dist(a1, a2, c1, c2), dist(c1, c2, b1, b2)
            s = (A + B + C) / 2
            return (abs(s*(s-A)*(s-B)*(s-C)))**0.5
        best = 0
        for p1 in points:
            for p2 in points:
                if p1 != p2:

                    for p3 in points:
                        if p1!= p3!= p2:
                            best = max(best, area(p1, p2, p3))
        return best
