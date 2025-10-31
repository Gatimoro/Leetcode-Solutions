# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        odd, even = 0, 0 
        bif_off = 0
        for i, [a, b] in enumerate(pairwise(arr)):
            if a * (-1) ** i < b * (-1) ** i:
                odd += 1
            else: odd = 0
            if b * (-1) ** i < a * (-1) ** i:
                even += 1
            else: even = 0
            bif_off = max(bif_off, even, odd)
        return bif_off + 1
