class Solution:
    def countOdds(self, low: int, high: int) -> int:
        d=high-low+1
        if low%2==1: d+=1
        return d//2
"""count how many odd numbers exist in the range low to high inclusive"""
