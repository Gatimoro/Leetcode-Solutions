class Solution:"""Checks if a number 2 times greater than another number is present in the array"""
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)-1):
            if not arr[i]%2 and arr[i]//2 in arr[i+1:] or arr[i]*2 in arr[i+1:]:
                return True
        return False
