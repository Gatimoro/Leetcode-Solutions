class Solution:
    def tribonacci(self, n: int) -> int:
        tfir=0
        tsec=tthir=1
        if n<2:
            return n
        for _ in range(n-2):
            tfir, tsec, tthir = tsec, tthir, tfir+tsec+tthir
        return tthir
"""The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn."""
