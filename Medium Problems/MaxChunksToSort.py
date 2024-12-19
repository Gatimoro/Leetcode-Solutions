class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        top , splits = 0 , 0
        for i,n in enumerate(arr):
            top = max(top,n)
            if top == i:
                splits += 1
        return splits
