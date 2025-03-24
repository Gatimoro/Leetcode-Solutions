class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        leng = len(arr) - 1
        l,r = 0, leng
        while l<r:
            m = (l+r) >> 1
            if m!= leng and arr[m] < arr[m+1]:
                l = m+1
            elif m != 0 and arr[m] < arr[m-1]:
                r = m-1
            else:
                return m
        return l
"""You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity."""
