class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        x=len(arr)
        Found=False
        n=(x>>1)
        i=x>>2
        while not Found:
            if arr[n+1]<arr[n]>arr[n-1]:
                return n
            if arr[n+1]<arr[n]:
                n=n-i
            else:
                n=n+i
            i=(i>>1)
            if not i:
                i=1
