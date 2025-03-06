class Solution:
    def coloredCells(self, n: int) -> int:
        return n ** 2 + (n-1) ** 2
"""There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Return cell count after n minutes."""
