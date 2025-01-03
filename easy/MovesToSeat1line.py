class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([abs(i-j) for i,j in zip(sorted(students),sorted(seats))])
"we have as many students as seats and each time a student moves up or down we count it as a move. This program returns the min amount of moves we need to make to seat everyone."
