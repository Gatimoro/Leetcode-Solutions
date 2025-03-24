class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        gap = 0
        best_gap = 0
        a, b = seats.index(1), list(reversed(seats)).index(1)
        print(a,b)
        for taken in range(a+1, len(seats) - b):
            if seats[taken]:
                gap = 0
            else:
                gap+=1
                if gap>best_gap:
                    best_gap = gap
        return max((best_gap + 1) >> 1, a,b)
"""You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person."""
