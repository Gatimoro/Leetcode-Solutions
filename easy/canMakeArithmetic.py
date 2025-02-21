class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        c=arr[0]
        diff = arr[1]-c
        for n in range(1,len(arr)):
            c+=diff
            if arr[n]!=c:return False
        return True
"""A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false."""
