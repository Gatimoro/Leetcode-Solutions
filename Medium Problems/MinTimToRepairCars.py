class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        import math
        guess=min(ranks)*cars**2  """APPROACH: BINARY GUESS"""
        jump=guess>>1
        tot=0
        while True:
            tot=0
            for x in ranks:
                tot+=math.isqrt( (guess-jump) // x)
                if tot>=cars:
                    break
            if tot>=cars:
                guess-=jump
            elif jump==1:
                return guess
            jump = jump>>1 or 1
        """DESCRIPTION: 
        You are given an integer array ranks representing the ranks of some mechanics. ranks[i] is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.

    You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

    Return the minimum time taken to repair all the cars.

    Note: All the mechanics can repair the cars simultaneously."""
