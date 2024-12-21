class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum([1 for B , S in zip(accumulate(arr,max),list(reversed(list(accumulate(reversed(arr),min))))[1:]) if B<=S])+1
        """Very happy to have come up with this. This one liner beats 90 percent of submissions.""
      """The strategy is the count all instances where the max number to the left including the number is less than or equal to the minimum number to the right of the number. Achieved through the use of accumulate() to keep track of the max and min."""
    
      
      """Description:
      You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array."""
