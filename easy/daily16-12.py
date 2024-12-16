class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hep=[]
        for i in range(len(nums)):
            hep.append([nums[i],i])
        heapify(hep)
        for o in range(k):
            hold=heappop(hep)
            heappush(hep,[hold[0]*multiplier,hold[1]])
        for i in hep:
            nums[i[1]]=i[0]
        return nums
"""Description:
          You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

 """
