class Solution:
    def findInMountainArray(self, target: int, MountainArr: 'MountainArray') -> int:
        l, r = 0, MountainArr.length() - 1
        
        while l < r:
            m = (l + r) // 2
            if MountainArr.get(m) < MountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        
        peak = l
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            mid = MountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
      
        l, r = peak + 1, MountainArr.length() - 1
        while l <= r:
            m = (l + r) // 2
            mid = MountainArr.get(m)
            if mid == target:
                return m
            elif mid < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
"""(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification."""
